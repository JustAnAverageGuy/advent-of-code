import aoc_helper

raw = aoc_helper.fetch(3, 2024)

import re
def parse_raw(raw: str):
    return raw

data = parse_raw(raw)

def part_one(data=data):
    return sum(int(i)*int(j) for i,j in re.findall(r'mul\((\d+),(\d+)\)', data))

aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)

def part_two(data=data):
    hmm = re.findall(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))", data)
    s = 0
    isen = True
    for i,j,k in hmm:
        if i == "don't()": isen = False; continue
        if i == "do()": isen = True; continue
        if isen:
            s += int(j)*int(k)
    return s

aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
