import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)

raw = aoc_helper.fetch(6, 2022)


def parse_raw():
    return raw.replace('\n', '')


data = parse_raw()


def part_one():
    i = 0
    while True:
        if len(set(data[i:i+4])) == 4:
            return i+4
        i += 1


def part_two():
    i = 1540  # part one answer just to speed up slightly :)
    while True:
        if len(set(data[i:i+14])) == 14:
            return i+14
        i += 1


aoc_helper.lazy_submit(day=6, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=6, year=2022, solution=part_two)
