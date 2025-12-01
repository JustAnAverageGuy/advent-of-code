import aoc_helper

raw = aoc_helper.fetch(1, 2025)


def parse_raw(raw: str):
    res = []
    for line in raw.splitlines():
        dirn, turn = line[0], int(line[1:])
        res.append(((dirn == "R") * 2 - 1, turn))
    return res


data = parse_raw(raw)


def part_one(data=data):
    ang = 50
    cnt = 0
    for dirn, turn in data:
        ang += dirn * turn
        ang %= 100
        cnt += ang == 0

    return cnt


aoc_helper.lazy_test(day=1, year=2025, parse=parse_raw, solution=part_one)


def part_two(data=data):
    ang = 50
    cnt = 0
    for dirn, turn in data:
        if dirn == 1:
            l = (ang // 100) + 1
            r = (ang + turn) // 100
        else:
            r = (ang + 99) // 100 - 1
            l = (ang - turn + 99) // 100
        cnt += r - l + 1
        ang += dirn * turn
        ang %= 100

    return cnt


aoc_helper.lazy_test(day=1, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2025, solution=part_two, data=data)
