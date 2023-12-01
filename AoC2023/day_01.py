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

raw = aoc_helper.fetch(1, 2023)


def parse_raw(raw):
    return raw.splitlines()


data = parse_raw(raw)


def part_one(data):
    s = 0
    for i in data:
        digs = []
        for j in i:
            if j in "1234567890": digs.append(j)
        s += int(digs[0]+digs[-1])
    return s

aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_one)


def part_two(data):
    s = 0
    dig = ["one","two","three","four","five","six","seven","eight","nine"]
    for i in data:
        digs = []
        for j in range(len(i)):
            if i[j] in "1234567890": digs.append(i[j])
            for k in dig:
                if i[j:].startswith(k):
                    digs.append(str(dig.index(k)+1))
        s += int(digs[0]+digs[-1])
    return s


aoc_helper.lazy_test(day=1, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2023, solution=part_two, data=data)
