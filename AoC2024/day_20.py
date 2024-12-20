from collections import Counter, defaultdict, deque
from itertools import product

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

raw = aoc_helper.fetch(20, 2024)


def parse_raw(raw: str):
    grid  = Grid.from_string(raw, lambda x: {".":0,"#":1,"S":2,"E":3}[x])
    start = list(grid.find_all(SparseGrid.from_string("2", default_factory=int)))[0]
    end   = list(grid.find_all(SparseGrid.from_string("3", default_factory=int)))[0]
    grid[start[1]][start[0]] = 0
    grid[end[1]][end[0]] = 0
    return (start, end, grid)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

def part_one(data=data):
    start, end, grid = data
    distances = {}
    qu = deque([(0, start)])
    while qu:
        d, (x,y) = qu.popleft()
        # if distances[(x,y)] < d: assert False, "There exist multiple paths, Eric lied"
        if (x,y) in distances: continue
        distances[(x,y)] = d
        for (nx, ny), v in grid.orthogonal_neighbours(x,y):
            if v != 1 and ((nx, ny) not in distances):
                qu.append((d+1, (nx,ny)))

    diamond2 = {
        (0,2), (1,1), (2,0),
        (0,-2), (1,-1), (-2,0),
        (-1,-1), (-1,1),
    }
    c = 0
    for (x,y) in distances:
        cur = distances[(x,y)]
        for dx, dy in diamond2:
            nx, ny = x + dx, y + dy
            if (nx, ny) in distances:
                nei = distances[(nx,ny)]
                gain = (nei - cur - 2)
                if gain >= 100:
                    c += 1
    return c


aoc_helper.lazy_test(day=20, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

def part_two(data=data):
    start, end, grid = data
    distances = {}
    qu = deque([(0, start)])
    while qu:
        d, (x,y) = qu.popleft()
        # if distances[(x,y)] < d: assert False, "There exist multiple paths, Eric lied"
        if (x,y) in distances: continue
        distances[(x,y)] = d
        for (nx, ny), v in grid.orthogonal_neighbours(x,y):
            if v != 1 and ((nx, ny) not in distances):
                qu.append((d+1, (nx,ny)))


    good_cheat = set()
    for (x,y) in distances:
        cur = distances[(x,y)]
        for dx, dy in product(range(-20, 21),repeat=2):
            if abs(dx) + abs(dy) > 20: continue
            nx, ny = x + dx, y + dy
            if (nx, ny) in distances:
                nei = distances[(nx,ny)]
                gain = (nei - cur - (abs(dx) + abs(dy)))
                if gain >= 100:
                    good_cheat.add((cur, (nx,ny)))
    return len(good_cheat)


aoc_helper.lazy_test(day=20, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=20, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=20, year=2024, solution=part_two, data=data)
