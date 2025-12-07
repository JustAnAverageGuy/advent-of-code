from collections import defaultdict

import aoc_helper
from aoc_helper import (
    Grid,
)

raw = aoc_helper.fetch(7, 2025)


def parse_raw(raw: str):
    return Grid.from_string(raw, classify=lambda x: {"S": 2, ".": 0, "^": 1}[x])


data = parse_raw(raw)


def part_one(data=data):
    # is_beam = [[False]*data.width for _ in range(data.height)]
    x, y = [*data.find_all(2)][0]
    splittings = 0
    beams = {x}
    while True:
        new_beams = set()
        y += 1
        if y == data.height:
            break
        for x in beams:
            if data.get(x, y) == 0:
                new_beams.add(x)
            elif data.get(x, y) == 1:
                splittings += 1
                if x - 1 >= 0:
                    new_beams.add(x - 1)
                if x + 1 < data.width:
                    new_beams.add(x + 1)
        beams = new_beams.copy()
    return splittings


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_one)


def part_two(data=data):
    x, y = [*data.find_all(2)][0]
    beams = {x: 1}
    while True:
        new_beams = defaultdict(int)
        y += 1
        if y == data.height:
            break
        for x in beams:
            if data.get(x, y) == 0:
                new_beams[x] += beams[x]
            elif data.get(x, y) == 1:
                if x - 1 >= 0:
                    new_beams[x - 1] += beams[x]
                if x + 1 < data.width:
                    new_beams[x + 1] += beams[x]
        beams = new_beams.copy()
    return sum(beams.values())


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2025, solution=part_two, data=data)
