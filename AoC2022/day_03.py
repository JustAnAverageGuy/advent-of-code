import aoc_helper


raw = aoc_helper.fetch(3, 2022)


def parse_raw():
    return [(i[:len(i)//2], i[len(i)//2:]) for i in raw.splitlines()]


data = parse_raw()


def priority(c: set[str]):
    c = list(c)[0]
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


def part_one():
    return sum(map(lambda x: priority(set(x[0]).intersection(set(x[1]))), data))


def part_two():
    return sum(map(lambda x: priority(x[0].intersection(x[1]).intersection(x[2])), (list(map(set, map(lambda x: x[0]+x[1], data[i:i+3]))) for i in range(0, len(data), 3))))


aoc_helper.lazy_submit(day=3, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=3, year=2022, solution=part_two)
