from collections import Counter, defaultdict, deque
import sys

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

raw = aoc_helper.fetch(6, 2024)


def parse_raw(raw: str):
    return Grid.from_string(raw, classify=lambda x: (0 if x == '.' else (1 if x == '#' else 2)))


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    n = len(data.data)
    cur = (-1,-1)
    
    for y in range(n):
        for x in range(n):
            if data[y][x] == 2:
                cur = (x,y)
                data[y][x] = 0
                break
        else:
            continue
        break

    dirn = (0, -1)
    nex_dir = lambda dir: {(0,-1):(1,0), (1,0):(0,1),(0,1):(-1,0), (-1,0):(0,-1)}[dir]
    visited = set()
    while 0<=cur[0]<=n-1 and 0<=cur[1]<=n-1:
        visited.add(tuple(cur))
        nxt = (cur[0]+dirn[0], cur[1]+dirn[1])
        if not all((0 <= i <= n-1) for i in nxt): break
        if data[nxt[1]][nxt[0]] == 1: dirn = nex_dir(dirn)
        else:
            cur = nxt
    return len(visited)






aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    n = len(data.data)
    start = (-1,-1)
    cur = [-1,-1]
    
    for y in range(n):
        for x in range(n):
            if data[y][x] == 2:
                start = (x,y)
                data[y][x] = 0
                break
        else:
            continue
        break

    nex_dir = lambda dir: {(0,-1):(1,0), (1,0):(0,1),(0,1):(-1,0), (-1,0):(0,-1)}[dir]

    dirn = (0, -1)
    cur = start
    visited = set()

    while 0<=cur[0]<=n-1 and 0<=cur[1]<=n-1:
        visited.add(tuple(cur))
        nxt = (cur[0]+dirn[0], cur[1]+dirn[1])
        if not all((0 <= i <= n-1) for i in nxt): break
        if data[nxt[1]][nxt[0]] == 1: dirn = nex_dir(dirn)
        else:
            cur = nxt

    ans = 0
    r = 0
    for v in visited:
        # imagine placing an obstruction there

        if v == start: continue

        print("\033[0GHere",r,ans, file=sys.stdout)
        r+=1

        dirn = (0, -1)
        cur = start
        state = set()
        data[v[1]][v[0]] = 1 # clean this up after the simulation

        while 0<=cur[0]<=n-1 and 0<=cur[1]<=n-1:
            curstate = (cur, dirn)
            if  curstate in state:
                data[v[1]][v[0]] = 0
                ans += 1
                break
            state.add(curstate)
            nxt = (cur[0]+dirn[0], cur[1]+dirn[1])
            if not all((0 <= i <= n-1) for i in nxt): 
                data[v[1]][v[0]] = 0
                break
            if data[nxt[1]][nxt[0]] == 1: dirn = nex_dir(dirn)
            else:
                cur = nxt
    return ans

aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2024, solution=part_two, data=data)
