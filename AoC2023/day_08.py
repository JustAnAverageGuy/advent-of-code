from math import lcm
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
from colorist import *

import sys
DAY = 8
YEAR = 2023

EXAMPLE = "EXAMPLE" in sys.argv
TWO = "2" in sys.argv

if EXAMPLE:
    if TWO:
        raw, answer = aoc_helper.get_sample_input(day=DAY, year=YEAR, part=2)
    else: 
        raw, answer = aoc_helper.get_sample_input(day=DAY, year=YEAR, part=1)
else:
    raw = aoc_helper.fetch(DAY, YEAR)

instructions, grph = raw.split('\n\n')

graph = dict()

import re

# print(instructions)

for i in grph.splitlines():
    p,lc,rc = re.match(r'(\w+) = \((\w+), (\w+)\)', i).groups()
    graph[p] = (lc,rc)

from itertools import cycle

curr = "AAA"
dirn = cycle(instructions)

cnt = 0


for i in  dirn:
    # break
    # if cnt % 1000 == 0: print(cnt)
    if curr == 'ZZZ': break
    curr = graph[curr][(i=='R')]
    cnt += 1

print(f'Part 1: {BrightColor.CYAN}{cnt}{BrightColor.OFF}')

A_nodes = [i for i in graph if i[-1] == 'A']

def inspect_cycles(start):
    dirn = cycle(instructions)
    curr = start
    cnt = 0
    
    visit_times = []
    for i in dirn:
        if curr[-1] == 'Z':
            visit_times.append((curr,cnt))
            if len(visit_times) == 10: return visit_times
        curr = graph[curr][(i=='R')]
        cnt += 1
            
# After seeing the number of A_nodes
# and the cycles they end up in, we see that they end up in 1 to 1 cycles 
# with the corresponding Z_nodes
# So we just need to take lcms of the visit time (actually should have taken
# the lcm of 2-cycle)

print(f'Part 2: {BrightColor.CYAN}{lcm(*[inspect_cycles(i)[0][1] for i in A_nodes])}{BrightColor.OFF}')