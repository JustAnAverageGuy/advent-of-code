from collections import Counter, defaultdict, deque
from itertools import count
from math import prod

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

raw = aoc_helper.fetch(14, 2024)


def parse_raw(raw: str):
    ans = [(extract_ints(i)) for i in raw.splitlines()]
    return ans


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

def after_n_steps(n, robots, box):
    W,H = box
    ok = []
    for px,py,vx,vy in robots:
        ok.append((
            (px + vx * (n)) % W,
            (py + vy * (n)) % H,
        ))
    return ok

def part_one(data=data):
    W,H = 101,103
    after = after_n_steps(100, data, (W,H))
    hmm = [0]*4

    # kk = [["."]*W for _ in range(H) ]

    # for x,y,_,_ in data:
    #     if kk[y][x] == '.':
    #         kk[y][x] = 1
    #     else:
    #         kk[y][x] += 1
    # for k in kk:
    #     print(*k, sep="")
    # return 

    for x,y in after:
        # if kk[y][x] == '.':
        #     kk[y][x] = 1
        # else:
        #     kk[y][x] += 1
        if x == W//2: continue
        if y == H//2: continue

        xx = x < (W//2)
        yy = y < (H//2)
        hmm[xx*2+yy] += 1
    # for k in kk: print(*k,sep='')
    return prod(hmm)



# aoc_helper.lazy_test(day=14, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    W,H = 101,103
    for t in count(1):
        kk = [["."]*W for _ in range(H) ]
        d = after_n_steps(t, data, (W,H))
        for x,y in d:
            if kk[y][x] == '.':
                kk[y][x] = 1
            else:
                kk[y][x] += 1
                break
        else:
            print(f'-------{t}--------')
            for k in kk: print(*k,sep='')
    return None


part_two(data)

