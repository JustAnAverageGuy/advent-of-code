from collections import Counter, defaultdict, deque
from functools import cache

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

# raw = aoc_helper.fetch(10, 2024)

with open("10.in") as f: raw = f.read()


def parse_raw(raw: str):
    return Grid.from_string(raw)


data = parse_raw(raw)



@cache
def which_are_reachable( stx, sty):
    x,y = stx, sty
    ans = set()
    if data[y][x] == 9: return frozenset({(x,y)})
    for (nx,ny),nv in data.orthogonal_neighbours(x,y):
        if nv == data[y][x] + 1:
            ans.update(which_are_reachable(nx,ny))
    return frozenset(ans)


def part_one(data=data):
    s = data.find_all(SparseGrid.from_string("0", default_factory=lambda :0))
    ans = 0
    for x,y in s:
        k = which_are_reachable(x,y)
        # print((x,y),k)
        ans += len(k)
    return ans





# aoc_helper.lazy_test(day=10, year=2024, parse=parse_raw, solution=part_one)


@cache
def which_are_reachable2( stx, sty):
    x,y = stx, sty
    ans = 0
    if data[y][x] == 9: return 1
    for (nx,ny),nv in data.orthogonal_neighbours(x,y):
        if nv == data[y][x] + 1:
            ans += (which_are_reachable2(nx,ny))
    return (ans)

def part_two(data=data):
    s = data.find_all(SparseGrid.from_string("0", default_factory=lambda :0))
    ans = 0
    for x,y in s:
        k = which_are_reachable2(x,y)
        # print((x,y),k)
        ans += k
    return ans

print(part_one(data))
print(part_two(data))


# aoc_helper.lazy_test(day=10, year=2024, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=10, year=2024, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=10, year=2024, solution=part_two, data=data)
