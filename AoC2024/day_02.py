import aoc_helper
from aoc_helper import (
    extract_ints, 
)

raw = aoc_helper.fetch(2, 2024)


def parse_raw(raw: str):
    return [extract_ints(i) for i in raw.splitlines()]


data = parse_raw(raw)


def issafe(l):
    diffs = [(j - i) for i, j in zip(l, l[1:])]
    return (-3 <= min(diffs) and max(diffs) <= -1) or (1 <= min(diffs) and max(diffs) <= 3)


def part_one(data=data):
    return sum(issafe(i) for i in data)


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    s = 0
    for i in data:
        if issafe(i):
            s += 1
            continue
        for j in range(len(data)):
            newdat = i[:j] + i[j + 1:]
            if issafe(newdat):
                s += 1
                break
    return s


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
