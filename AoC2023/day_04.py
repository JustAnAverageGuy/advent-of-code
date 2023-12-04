import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)

raw = aoc_helper.fetch(4, 2023)


def parse_raw(raw):
    cards = []
    for i in raw.splitlines():
        id, c = i.split(":")
        
        win, mine = c.split('|')
        cards.append((extract_ints(id)[0],extract_ints(win), extract_ints(mine)))
    return cards


data = parse_raw(raw)


def part_one(data):
    sm = 0
    for id, win, mine in data:
        t = len(set(win)&set(mine))
        if t:  
            t -= 1
            sm += (1<<t)
    return sm


aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_one)



def part_two(data):
    N = len(data)
    tot_counts = {i: 1 for i in range(N)}
    for j in range(N):
        # assert data[j][0] == j
        id, win, mine  = data[j]
        t = len(set(win)&set(mine))
        if t:
            for i in range(j+1,j+t+1):
                if i >= N: break
                tot_counts[i] += tot_counts[j]
    return sum(tot_counts.values())

aoc_helper.lazy_test(day=4, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2023, solution=part_two, data=data)
