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

import bisect

from tqdm import tqdm

raw = aoc_helper.fetch(15, 2022)

def log(func):
    def wrapper(*args, **kwargs):
        print(f'Calling: {func.__name__}(args={args},kwargs={kwargs})')
        result = func(*args,**kwargs)
        print(f'{result=}')
        return result
    return wrapper

def parse_raw(raw):
    pairs = dict()
    for i in raw.splitlines():
        sx,sy, bx,by = extract_ints(i)
        pairs[(sx,sy)] = (bx,by)
    return pairs


data = parse_raw(raw)
# print(data)

def manhattan(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

def break_range(range, px):
    l,r = range
    hmm = []
    if l <= px-1: hmm.append((l,px-1))
    if r >= px+1: hmm.append((px+1,r))
    return hmm


def fix_ranges(ranges):
    ranges.sort()
    fixed = []
    if ranges:
        l_,r_ = ranges[0]
        
        curl, curr = l_,r_
        
        
        for l,r in ranges[1:]:
            if curr <= l-2:
                fixed.append((curl, curr))
                curl, curr = l,r
            else:
                curr = max(curr, r)
        if not fixed or fixed[-1]!= (curl, curr): fixed.append((curl, curr))
    return fixed

def part_one(data):
    y = 2000000
    all_ranges = []
    for sensor, beacon in data.items():
        sx,sy = sensor
        d = manhattan(sensor, beacon)
        rad = d - abs(y-sy)
        if rad <= 0: continue
        
        ranges = [(sx - rad, sx + rad)]
        if beacon[1] == y: ranges = break_range(ranges[0], beacon[0])
        all_ranges.extend(ranges)
    all_ranges = fix_ranges(all_ranges)
    return sum(r-l+1 for (l,r) in all_ranges)


# aoc_helper.lazy_test(day=15, year=2022, parse=parse_raw, solution=part_one)

def check(data, y, N):
    all_ranges = []
    for sensor, beacon in data.items():
        sx,sy = sensor
        d = manhattan(sensor, beacon)
        rad = d - abs(y-sy)
        if rad <= 0: continue
        
        ranges = [(sx - rad, sx + rad)]
        if beacon[1] == y: ranges = break_range(ranges[0], beacon[0])
        all_ranges.extend(ranges)
    all_ranges = fix_ranges(all_ranges)
    
    intersected = []
    for l,r in all_ranges:
        ll = max(l, 0)
        rr = min(r, N)
        if ll <= rr: intersected.append((ll,rr))
        
    k = sum(r-l+1 for (l,r) in intersected)
    if k == N:
        if intersected[0][1] != N: return intersected[0][1] + 1
        return 0
        
    return False
    
    

def part_two(data):
    N = int(4e6)
    # N = 20
    for y in tqdm(range(0,N+1)):
        t = check(data,y,N)
        if t != False and (t,y) not in data.values(): 
            return (N*t + y) 
        # print(y, t)

# part_two(data)
# aoc_helper.lazy_test(day=15, year=2022, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=15, year=2022, solution=part_one, data=data)
aoc_helper.lazy_submit(day=15, year=2022, solution=part_two, data=data)
