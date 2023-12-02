from collections import defaultdict
import aoc_helper
from aoc_helper import (
    extract_ints,
    list,
)

raw = aoc_helper.fetch(2, 2023)

def extract_rgb(s):
    s = s.split(',')
    red, green, blue = 0,0,0
    for i in s:
        k = extract_ints(i)[0]
        if "red" in i: red = k
        if "green" in i: green = k
        if "blue" in i: blue = k
    return (red, green, blue)

def parse_raw(raw):
    games = defaultdict(list)
    for i in raw.splitlines():
        j = i.split(':')
        id = extract_ints(j[0])[0]
        j = j[1].split(";")
        for k in j: games[id].append(extract_rgb(k))
    return games


data = parse_raw(raw)


def part_one(data):
    sid = 0
    for id, game in data.items():
        if all((j[0]<= 12 and j[1]<= 13 and j[2] <= 14) for j in game):
            sid += id
    return sid

aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_one)


def part_two(data):
    spow = 0
    for id, game in data.items():
        min_r = 0
        min_g = 0
        min_b = 0
        for k in game:
            min_r = max(min_r, k[0])
            min_g = max(min_g, k[1])
            min_b = max(min_b, k[2])
        spow += min_r*min_g*min_b
    return spow

aoc_helper.lazy_test(day=2, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2023, solution=part_two, data=data)
