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

raw = aoc_helper.fetch(13, 2024)


def parse_raw(raw: str):
    mach = raw.split("\n\n")
    hmm = []

    for m in mach:
        cur = []
        for x in m.splitlines():
            cur.append(extract_ints(x))
        hmm.append(cur)
    
    return hmm


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    tok = 0
    cnt = 0
    for a,b,p in data:
        # dbrute = None
        # for x in range(101):
        #     for y in range(101):
        #         xx = x * a[0] + y * b[0]
        #         yy = x * a[1] + y * b[1]
        #         if xx == p[0] and yy == p[1]:
        #             k = 3 * x + y
        #             if dbrute is not None: dbrute = min(k, dbrute)
        #             else: dbrute = k


        d = a[0]*b[1] - a[1]*b[0]
        if d != 0:
            lm = (p[0] * b[1] - p[1] * b[0]) # divide this by d
            um = (-p[0] * a[1] + p[1] * a[0]) # divide this by d
            if (lm % d  or um %d ): 
                # if dbrute is not None: print(a,b,p,dbrute, lm, um)
                continue
            lm //= d
            um //= d
            if not (0 <= lm <= 100 and 0 <= um <= 100): 
                # if dbrute is not None: print(a,b,p,dbrute, lm, um)
                continue
            # print(lm, um, (a,b,p))
            # if dbrute is None: 
                # print(a,b,p,lm,um)
            tok += 3 * lm + um
            cnt += 1
            continue
        # d is zero
        assert False

    return tok

            




aoc_helper.lazy_test(day=13, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    tok = 0
    cnt = 0
    for a,b,p in data:
        d = a[0]*b[1] - a[1]*b[0]
        if d != 0:
            p[0] += 10000000000000
            p[1] += 10000000000000
            lm = (p[0]  * b[1] - p[1] * b[0]) # divide this by d
            um = (-p[0] * a[1] + p[1] * a[0]) # divide this by d
            if (lm % d  or um %d ): continue
            lm //= d
            um //= d
            if lm < 0 or um < 0: continue
            tok += 3 * lm + um
            cnt += 1
            continue
        # d is zero
        assert False

    return tok

aoc_helper.lazy_test(day=13, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=13, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=13, year=2024, solution=part_two, data=data)
