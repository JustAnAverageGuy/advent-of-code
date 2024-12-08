from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

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

raw = aoc_helper.fetch(8, 2024)



def parse_raw(raw: str):
    d = defaultdict(list)
    lines = raw.splitlines()
    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if j != '.': d[j].append((y,x))
    return d, (len(lines), len(lines[0]))


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    d, (h, w) = data
    anitnodes = set()
    for j in d.values():
        for a, b in combinations(j, 2):
            (y1,x1) = a
            (y2,x2) = b
            
            # 2*b-a
            anti1 = (2*y2-y1, 2*x2-x1)
            # 2*a-b
            anti2 = (2*y1-y2, 2*x1-x2)

            for x,y in [anti1,anti2]:
                if 0<= x < w and 0 <= y < h: anitnodes.add((y,x))
    return len(anitnodes)




aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    d, (h, w) = data
    anitnodes = set()
    for j in d.values():
        for a, b in permutations(j, 2):
            (y1,x1) = a
            (y2,x2) = b
            
            y,x = y1,x1

            dlta = y2-y1, x2-x1

            while (0<= x < w) and (0 <= y < h): 
                anitnodes.add((y,x))
                x += dlta[1]
                y += dlta[0]
    return len(anitnodes)


aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2024, solution=part_two, data=data)
