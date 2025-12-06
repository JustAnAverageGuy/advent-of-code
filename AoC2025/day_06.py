from math import prod

import aoc_helper

raw = aoc_helper.fetch(6, 2025)


def parse_raw(raw: str):
    return [line for line in raw.splitlines()]


data = parse_raw(raw)


def part_one(data=data):
    data = [line.split() for line in data]
    ans = 0
    for j in range(len(data[0])):
        nums = [int(data[i][j]) for i in range(len(data) - 1)]
        op = data[-1][j]
        if op == "+":
            ans += sum(nums)
        else:
            ans += prod(nums)
    return ans


aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_one)


def part_two(data=data):
    op_posns = [i for i, j in enumerate(data[-1]) if j != " "]
    op_posns.append(len(data[0]) + 1)
    # print(op_posns)
    ans = 0
    for i, j in zip(op_posns, op_posns[1:]):
        nums = [
            int("".join(data[r][c] for r in range(len(data) - 1) if data[r][c] != " "))
            for c in range(j - 2, i - 1, -1)
        ]
        op = data[-1][i]
        if op == "+":
            ans += sum(nums)
        else:
            ans += prod(nums)
    return ans


aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2025, solution=part_two, data=data)
