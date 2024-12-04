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

raw = aoc_helper.fetch(1, 2024)


def parse_raw(raw: str):
    return [tuple(map(int,i.split()))  for i in raw.splitlines()]



data = parse_raw(raw)



# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    ls = [i[0] for i in data]
    rs = [i[1] for i in data]
    return sum(abs(i-j) for i,j in zip(sorted(ls), sorted(rs)))


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    ls = [i[0] for i in data]
    rs = [i[1] for i in data]
    c = Counter(rs)
    return sum(i*c[i] for i in ls)


aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2024, solution=part_two, data=data)
