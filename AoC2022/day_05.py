from aoc_helper import (
    Grid,
    PrioQueue,
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)
import aoc_helper
import re
raw = aoc_helper.fetch(5, 2022)

"""
# this function could have been used to avoid manual parsing of input

def parse_crates(f):
    lines = []
    while '1' not in (line := f.readline()):
        lines.append(line)
    n = int(line.strip().split()[-1])
    crates = []
    for i in range(n):
        crates.append([])
    while lines:
        line = lines.pop()
        for i in range(n):
            p = 1 + 4*i
            if p < len(line) and line[p] != ' ':
                crates[i].append(line[p])
    return crates
"""

def parse_raw():
    crates, steps = raw.split("\n\n")
    steps = list(map(extract_ints, steps.split('\n')))
    crates = [[], ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'], ['H', 'F', 'R'], ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'], ['Q', 'H', 'P', 'B', 'F', 'W', 'G'], [
        'P', 'S', 'M', 'J', 'H'], ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'], ['P', 'T', 'H', 'N', 'M', 'L'], ['F', 'D', 'Q', 'R'], ['D', 'S', 'C', 'N', 'L', 'P', 'H']]  # manually quicker
    return crates, steps


crates, steps = parse_raw()  # steps: move %d from %d to %d


def part_one():
    for i in steps:
        t = crates[i[1]][-i[0]:]
        crates[i[1]] = crates[i[1]][:-i[0]]
        crates[i[2]].extend(t[::-1])
    return ''.join(map(lambda x: x[-1] if len(x) else '', crates))


def part_two():
    for i in steps:
        t = crates[i[1]][-i[0]:]
        crates[i[1]] = crates[i[1]][:-i[0]]
        crates[i[2]].extend(t)
    return ''.join(map(lambda x: x[-1] if len(x) else '', crates))


aoc_helper.lazy_submit(day=5, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=5, year=2022, solution=part_two)
