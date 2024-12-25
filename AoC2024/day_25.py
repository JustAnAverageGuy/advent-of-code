from itertools import product

import aoc_helper


raw = aoc_helper.fetch(25, 2024)


def parse_raw(raw: str):
    schemas = []
    for scheme in raw.split("\n\n"):
        a = scheme.strip().splitlines()
        assert len(a) == 7
        if set(a[0]) == {"#"}:
            # it is a lock
            hs = [0]*5
            for x in range(5):
                for y in range(7):
                    if a[y][x] == '#': hs[x] = y
            schemas.append((0, tuple(hs)))
        else:
            # it is a key
            hs = [0]*5
            b = a[::-1]
            for x in range(5):
                for y in range(7):
                    if b[y][x] == '#': hs[x] = y
            schemas.append((1, tuple(hs)))
    return schemas



data = parse_raw(raw)



def part_one(data=data):
    sepa = [[],[]]
    for typ, x in data:
        sepa[typ].append(x)
    c = 0
    for l, r in product(*sepa):
        a = [i+j for i,j in zip(l,r)]
        c += max(a) <= 5
    return c




aoc_helper.lazy_test(day=25, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_submit(day=25, year=2024, solution=part_one, data=data)
