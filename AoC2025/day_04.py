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

raw = aoc_helper.fetch(4, 2025)


def parse_raw(raw: str):
    return Grid.from_string(raw,classify=lambda x: {'@':1, '.':0}[x]) 


data = parse_raw(raw)

def part_one(data=data):
    accessible = 0
    for y in range(data.height):
        for x in range(data.width):
            if not data.get(x,y): continue
            accessible += sum(v for _, v in data.neighbours(x,y)) <4
    return accessible



aoc_helper.lazy_test(day=4, year=2025, parse=parse_raw, solution=part_one)

def part_two(data=data):
    total_removed = 0
    while True:
        accessible = 0
        to_be_removed = []
        for y in range(data.height):
            for x in range(data.width):
                if not data.get(x,y): continue
                if not sum(v for _, v in data.neighbours(x,y)) <4: continue
                # for (nx,ny),_ in data.neighbours(x,y):
                to_be_removed.append((x,y))
        if not to_be_removed: break
        total_removed += len(to_be_removed)
        for x,y in to_be_removed: data[x,y] = 0
    return total_removed


aoc_helper.lazy_test(day=4, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2025, solution=part_two, data=data)
