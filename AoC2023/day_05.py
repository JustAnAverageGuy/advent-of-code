from colorist import *

import aoc_helper
from aoc_helper import (
    extract_ints,
    list,
    range,
)

import sys

EXAMPLE = "EXAMPLE" in sys.argv
TWO = "2" in sys.argv

if EXAMPLE:
    if TWO:
        raw, answer = aoc_helper.get_sample_input(day=5, year=2023, part=2)
    else: 
        raw, answer = aoc_helper.get_sample_input(day=5, year=2023, part=1)
else:
    raw = aoc_helper.fetch(5, 2023)
    

s = raw.split("\n\n")
seeds = extract_ints(s[0])

def x_to_y_map_1(description:str, inputs: list[int]):
    ranges  = [tuple(extract_ints(i)) for i in description.splitlines()[1:]]
    ans = []
    for i in inputs:
        for dest, sour, ln in ranges:
            if 0 <= (i - sour) <  ln:
                ans.append(dest + i - sour)
                break
        else:
            ans.append(i)
    return ans

# part 1
ok = seeds[::]

for hmm in s[1:]: ok = x_to_y_map_1(hmm, ok)

print(f"Part 1: {BrightColor.CYAN}{min(ok)}{BrightColor.OFF}")

# part 2

seed_ranges = list((seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2))

def strt_ln_to_strt_end(start, len): return (start, start + len - 1)
def strt_end_to_strt_ln(start, end): return (start, end - start + 1)
    


def intersect_ranges(range1, range2):
    """
        returns common, part_of_seed_not_intersecting
        range1 is the seed
        range2 is the source_map
    """
    strt1, end1 = strt_ln_to_strt_end(*range1)
    strt2, end2 = strt_ln_to_strt_end(*range2)
    
    strt, end = max(strt1, strt2), min(end1, end2)
    
    if end < strt: return [], [range1]
    
    diff =[]
    if strt1 < strt: diff.append(strt_end_to_strt_ln(strt1, strt-1))
    if   end < end1: diff.append(strt_end_to_strt_ln(end+1, end1))
    
    return [ strt_end_to_strt_ln(strt, end) ], diff

def x_to_y_map_2(description:str, inputs: list[tuple[int,int]]):
    ranges  = [tuple(extract_ints(i)) for i in description.splitlines()[1:]]
    ans = []
    
    not_handled = inputs[::]
    new_not_handled = []
    
    for dest, sour, ln in ranges:
        for seedrng in not_handled:
            
            comm, diff = intersect_ranges(seedrng, (sour, ln))
            if comm:
                ans.append((comm[0][0]+dest-sour, comm[0][1]))
            if diff:
                new_not_handled.extend(diff)
                
        not_handled = new_not_handled.copy()
        new_not_handled = []
    
    ans.extend(not_handled)
    return ans

ok = seed_ranges[::]

for hmm in s[1:]:  ok = x_to_y_map_2(hmm, ok)

print(f"Part 2: {BrightColor.CYAN}{min(ok)[0]}{BrightColor.OFF}")
