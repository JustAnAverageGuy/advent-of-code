from collections import  defaultdict 
import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
)

raw = aoc_helper.fetch(16, 2024)


def parse_raw(raw: str):
    return Grid.from_string(raw, lambda x: {".":0,"#":1,"S":2,"E":3}[x])


data = parse_raw(raw)


def part_one(data=data):
    S = list(data.find_all(SparseGrid.from_string("2", default_factory=int)))[0]
    E = list(data.find_all(SparseGrid.from_string("3", default_factory=int)))[0]
    data[S[1]][S[0]] = 0
    data[E[1]][E[0]] = 0

    qu = PrioQueue([(0, S, (1,0))])
    visited = set()
    for cost, (x,y), dirn in qu:
        if (x,y) == E: return cost
        if (x,y, dirn) in visited: continue
        visited.add((x,y,dirn))
        for (nx, ny), v in data.orthogonal_neighbours(x,y):
            if v == 1: continue
            dx, dy = (nx - x), (ny - y)
            new_cost  = 1001 if (dx,dy) != dirn else 1
            qu.push((cost + new_cost, (nx, ny), (dx, dy)))
    



with open("./example_16.in","r") as f:
    a,b = f.read().split("\n\n")
    example1 = (a.strip(), b.strip())

aoc_helper.lazy_test(day=16, year=2024, parse=parse_raw, solution=part_one, test_data=example1)



def part_two(data=data):
    S = list(data.find_all(SparseGrid.from_string("2", default_factory=int)))[0]
    E = list(data.find_all(SparseGrid.from_string("3", default_factory=int)))[0]
    data[S[1]][S[0]] = 0
    data[E[1]][E[0]] = 0

    qu = PrioQueue([(0, S, (1,0))])
    visited = set()
    prev = defaultdict(list)
    success = set()
    mincost = None
    for cost, (x,y), dirn in qu:
        if mincost is not None and (cost > mincost): break
        if (x,y) == E:
            if mincost is None: mincost = cost
            success.add((cost, (x,y), dirn))
            continue

        if (x,y, dirn) in visited: continue
        visited.add((x,y,dirn))
        for (nx, ny), v in data.orthogonal_neighbours(x,y):
            if v == 1: continue
            dx, dy = (nx - x), (ny - y)
            new_cost  = 1001 if (dx,dy) != dirn else 1
            new_state = (cost + new_cost, (nx, ny), (dx, dy))
            qu.push(new_state)
            prev[new_state].append((cost, (x,y), dirn))
    allpoints = set()
    hmm = [*success]
    while hmm:
        curr = hmm.pop()
        allpoints.add(curr[1])
        for x in prev[curr]: hmm.append(x)
    return len(allpoints)

aoc_helper.lazy_test(day=16, year=2024, parse=parse_raw, solution=part_two, test_data=(example1[0],"64"))

aoc_helper.lazy_submit(day=16, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=16, year=2024, solution=part_two, data=data)
