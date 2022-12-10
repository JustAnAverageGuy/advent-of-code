import aoc_helper
import re
from aoc_helper import (
    iter,
    range,
)

raw = aoc_helper.fetch(10, 2022)
#raw = open("sample_input.txt").read()


def parse_raw():
    global raw
    raw = re.sub(r'addx (-?\d+)', r'addx 0\naddx \1',
                 raw).replace("noop", "noop 0")
    return [(i.strip().split()[0], int(i.strip().split()[1])) for i in raw.splitlines()]


data = iter(parse_raw())


def part_one():
    cycle = 1
    i = data.next()
    X = 1
    s = 0
    while cycle <= 220:
        if cycle in [20 + 40*k for k in range(6)]:s += cycle * X
        cycle += 1
        X += i[1]
        i = data.next()
    print(s)
    return s


def part_two():
    cycle = 1
    i = data.next()
    monitor = ''
    X = 1
    while cycle <= 240:
        if ((cycle-1) % 40 in [X-1, X, X+1]):
            # Different Printintg Modes
            #monitor += '⬜🟨🟦'[[X-1,X,X+1].index((cycle-1)%40)]
            monitor += '🔲'
            #monitor += '⬜🟨🟦'[((cycle-1)//40) % 3]
        else:
            monitor += '⬛'

        if (cycle % 40 == 0):
            monitor += '\n'
        cycle += 1
        X += i[1]
        try:
            i = data.next()
        except StopIteration:
            i = ('noop', 0)
    print(monitor)


part_two()
#aoc_helper.lazy_submit(day=10, year=2022, solution=part_one)
#aoc_helper.lazy_submit(day=10, year=2022, solution=part_two)
