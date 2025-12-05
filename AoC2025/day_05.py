import aoc_helper

raw = aoc_helper.fetch(5, 2025)


def parse_raw(raw: str):
    ranges, ingredients = raw.split("\n\n")
    rs = []
    for s in ranges.splitlines():
        a, b = map(int, s.strip().split("-"))
        rs.append((a, b))
    ings = [int(i) for i in ingredients.split()]
    return rs, ings


data = parse_raw(raw)


def part_one(data=data):
    ranges, ingredients = data
    cnt = 0
    for i in ingredients:
        cnt += any(a <= i <= b for a, b in ranges)
    return cnt


aoc_helper.lazy_test(day=5, year=2025, parse=parse_raw, solution=part_one)


def part_two(data=data):
    ranges, _ = data
    ranges.sort()
    merged = [ranges[0]]
    for a, b in ranges[1:]:
        if merged[-1][1] >= a:
            x, y = merged.pop()
            merged.append((min(x, a), max(y, b)))
        else:
            merged.append((a,b))
    return sum(b-a+1 for a,b in merged)

aoc_helper.lazy_test(day=5, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2025, solution=part_two, data=data)
