from collections import Counter, defaultdict
from functools import cache

import aoc_helper
from aoc_helper import (
    extract_ints,
)

raw = aoc_helper.fetch(21, 2024)


def parse_raw(raw: str):
    return raw.splitlines()


data = parse_raw(raw)

def convert_string_to_pos(input_pad:str):
    ip = input_pad.splitlines()
    positions = {
        ip[i][j] : (j, i)
        for i in range(len(ip))
        for j in range(len(ip[0]))
        if ip[i][j] != " "
    }
    inv = {
        (j, i) : ip[i][j]
        for i in range(len(ip))
        for j in range(len(ip[0]))
        if ip[i][j] != " "
    }
    return positions, inv


numpad, inv_numpad = convert_string_to_pos(
"""789
456
123
 0A"""
)

dpad, inv_dpad = convert_string_to_pos(
""" ^A
<v>"""
)

dirn = {
    "^":(0, -1),
    "v":(0,  1),
    ">":(1,  0),
    "<":(-1, 0),
}

def interpret(start, operations, is_numpad=False):
    cx, cy = start
    out = []
    for i in operations:
        if i == 'A':
            if is_numpad:
                assert (cx, cy) in inv_numpad
                out.append(inv_numpad[(cx,cy)])
            else:
                assert (cx, cy) in inv_dpad
                out.append(inv_dpad[(cx,cy)])
            continue
        dx, dy = dirn[i]
        cx += dx
        cy += dy
    return (cx, cy), out

from itertools import combinations, product, pairwise

def paths_from_to(start:tuple[int, int], end:tuple[int, int]):
    """
    generates all paths from start to end and executing at end
    """
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    xchar = '>'
    ychar = 'v'
    if dx < 0:
        dx = -dx
        xchar = '<'
    if dy < 0:
        dy = -dy
        ychar = '^'
    n = dx+dy
    for c in combinations(range(n),dy):
        s = [xchar]*(n)
        s.append("A")
        for i in c: s[i] = ychar
        yield s

def shortest_path(start:tuple[int, int], end:tuple[int, int], is_dpad=True):
    """
    generates the shortest path from start to end and executing at end
    """
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    xchar = '>'
    ychar = 'v'
    if dx < 0:
        dx = -dx
        xchar = '<'
    if dy < 0:
        dy = -dy
        ychar = '^'

    ranking = '<v^>' # lower index means it is further from A, hence should be placed earlier

    # print(f'{start} -> {end}, dx: {xchar}, dy: {ychar}, dpad?: {is_dpad}')
    if not is_dpad:
        if start in {numpad[k] for k in "147"} and end in {numpad[k] for k in "0A"}:
            ranking = ">v"
            assert xchar in ranking and ychar in ranking
        elif start in {numpad[k] for k in "0A"} and end in {numpad[k] for k in "147"}:
            ranking = "^<"
            assert xchar in ranking and ychar in ranking

    else:
        if end in {dpad["<"]}:
            ranking = "v^<>"
            assert xchar in ranking and ychar in ranking
        elif start in {dpad["<"]}:
            ranking = "><^v"


    if ranking.find(xchar) > ranking.find(ychar):
        return ychar * dy + xchar * dx + "A"
    else:
        return xchar * dx + ychar * dy + "A"

def verify(target):
    s = "".join(heuristic("".join(heuristic("".join(heuristic(target, True))))))
    out = interpret(numpad["A"], interpret(dpad["A"], interpret(dpad["A"], s)[1])[1], True)[1]
    return list(target) == (out)

def gen_string(target, is_numpad=False):
    cur_dict = numpad if is_numpad else dpad
    target = "A"+target

    return product(
        *map(
            lambda x: paths_from_to( cur_dict[x[0]], cur_dict[x[1]]),
            pairwise(target)
        )
    )

def heuristic(target, is_numpad=False):
    cur_dict = numpad if is_numpad else dpad
    target = "A"+target
    # print(cur_dict)

    return list(map(lambda x: shortest_path( cur_dict[x[0]], cur_dict[x[1]], not is_numpad), pairwise(target)))

def part_one(data=data):
    s = 0
    for i in data:
        x = Counter()
        for k in pairwise("A"+i):
            x[k] += 1
        x = sove(x, True)
        for _ in range(2):
            x = sove(x)
        s += extract_ints(i)[0] * (sum(x.values()) )
    return s


aoc_helper.lazy_test(day=21, year=2024, parse=parse_raw, solution=part_one)


# could have extracted it out to a dictionary, but this is good enough
@cache
def best_move_from_to(is_numpad):
    ans:dict[tuple[str,str],tuple[defaultdict[tuple[str,str],int],str]] = {}
    cur_dict = numpad if is_numpad else dpad
    for i in cur_dict:
        for j in cur_dict:
            k = heuristic(i+j, is_numpad)[1] # ignoring the A -> i transition
            s = defaultdict(int)
            for x,y in pairwise(k): s[(x,y)] += 1
            ans[(i,j)] = (s, k[0])
    return ans
        
def sove(target, is_numpad=False):
    combined = Counter()
    for x, count in target.items():
        mapped, start = best_move_from_to(is_numpad)[x]
        for i,j in mapped.items():
            combined[i] += j * count
        combined["A", start] += count
    return combined





def part_two(data=data):
    s = 0
    for i in data:
        x = Counter()
        for k in pairwise("A"+i):
            x[k] += 1
        x = sove(x, True)
        for _ in range(25):
            x = sove(x)
        s += extract_ints(i)[0] * (sum(x.values()) )
    return s

aoc_helper.lazy_test(day=21, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=21, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=21, year=2024, solution=part_two, data=data)
