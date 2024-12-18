import aoc_helper
from aoc_helper import (
    Grid,
    extract_ints,
    list,
    range,
)

raw = aoc_helper.fetch(18, 2024)


def parse_raw(raw: str):
    data = []
    for line in raw.splitlines(): data.append(extract_ints(line))
    return data


data = parse_raw(raw)


def part_one(data=data):
    H,W = 71,71
    grid = Grid(list(list([0]*W) for _ in range(H) ))
    for x,y in data[:1024]:
        grid[y][x] = 1

    final_cost = grid.pathfind(
        start=(0,0),
        end=None,
        next_state=lambda _, dx, dy, cur, nex: None if nex == 1 else (),
        cost_function=lambda _,__: 1,
    )
    return (final_cost)


aoc_helper.lazy_test(day=18, year=2024, parse=parse_raw, solution=part_one)



def part_two(data=data):
    H,W = 71,71
    n = len(data)
    l,r = -1,n+1

    while r-l > 1:
        m = l + (r-l)//2
        grid = Grid(list(list([0]*W) for _ in range(H) ))

        for x,y in data[:m]: grid[y][x] = 1

        final_cost = grid.pathfind(
            start=(0,0),
            end=None,
            next_state=lambda _, dx, dy, cur, nex: None if nex == 1 else (),
            cost_function=lambda _,__: 1,
        )
        if final_cost is None:
            r = m
        else:
            l = m

    x,y = data[r-1] # rth element
    return f'{x},{y}'


aoc_helper.lazy_test(day=18, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=18, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=18, year=2024, solution=part_two, data=data)
