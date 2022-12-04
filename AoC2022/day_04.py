import aoc_helper
raw = aoc_helper.fetch(4, 2022)


def parse_raw():
    return [list(map(lambda x: tuple(map(int, x.split("-"))), i.split(","))) for i in raw.splitlines()]


data = parse_raw()


def part_one():
    count = 0
    for i in data:
        count += ((i[0][0] - i[1][0])*(i[0][1] - i[1][1]) <= 0)
    return count


aoc_helper


def isintersect(a, b, c, d):
    return ((a-c)*(b-d) <= 0) or (((b-c)*(a-d)) <= 0)


def part_two():
    count = 0
    for i in data:
        count += isintersect(i[0][0], i[0][1], i[1][0], i[1][1])
    return count


aoc_helper.lazy_submit(day=4, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=4, year=2022, solution=part_two)
