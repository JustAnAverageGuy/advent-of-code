from collections import Counter, defaultdict, deque

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
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(11, 2024)


def parse_raw(raw: str):
    return [int(i) for i in raw.split()]


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

def part_one(data=data):
    counts = defaultdict(int)
    for i in data: counts[i] += 1

    for i in range(25):
        nxt = defaultdict(int)
        for n,v in counts.items():
            if n == 0: nxt[1] += v
            elif len(str(n)) % 2 == 0:
                s = str(n)
                r,l = s[len(s)//2:],s[:len(s)//2]
                nxt[int(r)] += v
                nxt[int(l)] += v
            else:
                nxt[n*2024] += v
        counts = nxt.copy()

    return sum(counts.values())
            


aoc_helper.lazy_test(day=11, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    counts = defaultdict(int)
    for i in data: counts[i] += 1

    for i in range(75):
        nxt = defaultdict(int)
        for n,v in counts.items():
            if n == 0: nxt[1] += v
            elif len(str(n)) % 2 == 0:
                s = str(n)
                r,l = s[len(s)//2:],s[:len(s)//2]
                nxt[int(r)] += v
                nxt[int(l)] += v
            else:
                nxt[n*2024] += v
        counts = nxt.copy()
    return sum(counts.values())


aoc_helper.lazy_test(day=11, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2024, solution=part_two, data=data)
