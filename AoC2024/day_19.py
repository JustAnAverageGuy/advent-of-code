from functools import cache

import aoc_helper

raw = aoc_helper.fetch(19, 2024)

def parse_raw(raw: str):
    a, b = raw.split("\n\n")
    patterns = a.split(', ')
    designs = b.splitlines()
    return patterns, designs

data = parse_raw(raw)

def is_possible(x:str, patterns):
    if x == "": return True
    for i in patterns:
        if x.startswith(i):
            a = is_possible(x[len(i):],patterns)
            if a: return True
    return False

def part_one(data=data):
    patterns, designs = data
    # for each pattern check if it can be decomposed using others
    basis = []
    for i in range(len(patterns)):
        modif = [*patterns[:i], *patterns[i+1:]]
        if not is_possible(patterns[i], modif): basis.append(patterns[i])

    c = 0
    for i in designs:
        if is_possible(i, basis):
            c += 1
    return c

aoc_helper.lazy_test(day=19, year=2024, parse=parse_raw, solution=part_one)

# this caching for part 2 won't work with example input

patterns = data[0]
basis = []
for i in range(len(patterns)):
    modif = [*patterns[:i], *patterns[i+1:]]
    if not is_possible(patterns[i], modif): basis.append(patterns[i])

@cache
def count(x):
    # print(f"count({x})")
    if x == "": return 1
    if not is_possible(x, basis): return 0
    tot = 0
    for p in patterns:
        if x.startswith(p):
            tot += count(x[len(p):])
    return tot

def part_two(data=data):
    c = 0
    for i in data[1]: c += count(i)
    return c

# aoc_helper.lazy_test(day=19, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=19, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=19, year=2024, solution=part_two, data=data)
