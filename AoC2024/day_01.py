from collections import Counter
import aoc_helper

raw = aoc_helper.fetch(1, 2024)


def parse_raw(raw: str):
    return [tuple(map(int, i.split())) for i in raw.splitlines()]


data = parse_raw(raw)


def part_one(data=data):
    ls = [i[0] for i in data]
    rs = [i[1] for i in data]
    return sum(abs(i - j) for i, j in zip(sorted(ls), sorted(rs)))


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    ls = [i[0] for i in data]
    rs = [i[1] for i in data]
    c = Counter(rs)
    return sum(i * c[i] for i in ls)


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2024, solution=part_two, data=data)
