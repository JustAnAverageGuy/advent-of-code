from collections import Counter, defaultdict, deque

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

raw = aoc_helper.fetch(2, 2024)


def parse_raw(raw: str):
    return [extract_ints(i) for i in raw.splitlines()]


data = parse_raw(raw)

def issafe(l):
    diffs = [(j-i) for i,j in zip(l, l[1:])]
    if (-3<=min(diffs) and max(diffs) <= -1)  or (1<=min(diffs) and max(diffs) <= 3): return True
    return False


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    return sum(issafe(i) for i in data)


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    s = 0
    for i in data:
        if issafe(i): s += 1; continue
        for j in range(len(data)):
            newdat = i[:j]+i[j+1:]
            if issafe(newdat): s += 1; break
    return s



aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
