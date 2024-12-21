import aoc_helper
from aoc_helper import (
    extract_ints, 
)

raw = aoc_helper.fetch(5, 2024)


def parse_raw(raw: str):
    a, b = raw.split("\n\n")
    rules = [tuple(extract_ints(i)) for i in a.splitlines()]
    orders = [extract_ints(i) for i in b.splitlines()]
    return rules, orders


data = parse_raw(raw)


def check(rules: set[tuple[int, int]], order: list[int]):
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            a, b = (order[i], order[j])  # opposite order in
            if (b, a) in rules: return False
    return True


from functools import cmp_to_key  # my beloved


def part_one(data=data):
    rules, orders = data
    s = 0
    for i in orders:
        if check(rules, i):
            s += i[len(i) // 2]
    return s


aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    rules, orders = data
    s = 0

    def cmp(x, y):
        if (x, y) in rules: return -1
        if (y, x) in rules: return 1
        return 0

    for i in orders:
        if not check(rules, i):
            # sort it
            k = sorted(i, key=cmp_to_key(cmp))
            s += k[len(k) // 2]
    return s


aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2024, solution=part_two, data=data)
