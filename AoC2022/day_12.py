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
    range,
    tail_call,
)

import sys
from collections import deque
from typing import Tuple

raw = aoc_helper.fetch(12, 2022)
# raw = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""


def parse_raw(raw) -> Tuple[Tuple[int,int], Tuple[int,int], Grid[int]]:
    g = Grid([]).from_string(raw, ord)
    for i in range(len(g.data)):
        for j in range(len(g.data[0])):
            if g[i][j] == ord('S'): s = (j,i)
            if g[i][j] == ord('E'): e = (j,i)
    # print(s,e)
    g[s[1]][s[0]] = ord('a')
    g[e[1]][e[0]] = ord('z')
    return (s,e,g)


data = parse_raw(raw)

def bfs(start, end, grid:Grid):
    visited = set()
    inqueu  = set([start])
    qu = deque([(start,0)])
    
    while qu:
        curr, dist = qu.pop()
        visited.add(curr)
        inqueu.remove(curr)
        
        if curr == end: return dist
        
        for point, height in grid.orthogonal_neighbours(*curr):
            if point in visited or point in inqueu: continue
            if height <= grid[curr[1]][curr[0]]+1:
                qu.appendleft((point, dist + 1))
                inqueu.add(point)
    


def part_one(data:Tuple[Tuple[int,int], Tuple[int,int], Grid[int]]):
    return bfs(*data)
    
aoc_helper.lazy_test(day=12, year=2022, parse=parse_raw, solution=part_one)


def part_two(data):
    _,end,grid = data

    visited = set()
    inqueu  = set([end])
    qu = deque([(end,0)])
    
    while qu:
        curr, dist = qu.pop()
        visited.add(curr)
        inqueu.remove(curr)
        
        if grid[curr[1]][curr[0]] == ord('a'): return dist
        
        for point, height in grid.orthogonal_neighbours(*curr):
            if point in visited or point in inqueu: continue
            if height >= grid[curr[1]][curr[0]]-1:
                qu.appendleft((point, dist + 1))
                inqueu.add(point)    


aoc_helper.lazy_test(day=12, year=2022, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2022, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2022, solution=part_two, data=data)
