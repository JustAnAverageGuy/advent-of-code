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

raw = aoc_helper.fetch(3, 2024)


import re
def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    return sum(int(i)*int(j) for i,j in re.findall(r'mul\((\d+),(\d+)\)', data))



aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    hmm = re.findall(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))", data)
    s = 0
    isen = True
    for i,j,k in hmm:
        if i == "don't()": isen = False; continue
        if i == "do()": isen = True; continue
        if isen:
            s += int(j)*int(k)

    return s


aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
