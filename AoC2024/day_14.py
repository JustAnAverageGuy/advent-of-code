from math import prod
import aoc_helper
from aoc_helper import (
    extract_ints,
    range,
)

raw = aoc_helper.fetch(14, 2024)

import sys
raw = sys.stdin.read()


def parse_raw(raw: str):
    ans = [(extract_ints(i)) for i in raw.splitlines()]
    return ans


data = parse_raw(raw)

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


    for x,y in after:
        if x == W//2: continue
        if y == H//2: continue

        xx = x < (W//2)
        yy = y < (H//2)
        hmm[xx*2+yy] += 1
    return prod(hmm)


def part_two(data=data):
    W,H = 101,103
    for t in (range(1,W*H+1)):
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

