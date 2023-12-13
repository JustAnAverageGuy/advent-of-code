from itertools import groupby
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

import sys
from colorist import *

DAY = 12
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

springs = []

for line in raw.splitlines():
    pattrn, nonogram = line.split()
    nonogram = [int(i) for i in nonogram.split(',')]
    pattrn = [{'#':1,'.':0,'?':2}[i] for i in pattrn]
    springs.append((pattrn, nonogram))

# def count_ways(pattern, nonogram):

# print(*springs, sep='\n', file=sys.stderr)

def count_groups(s):
    return [len(list(i[1])) for i in groupby(s) if i[0] == 1]

# def bruteforce(pattern, nongram):
#     cnt = 0
    
#     bitmask = 0
#     base = 0
#     for i,x in enumerate(pattern):
#         if x == 2: bitmask |= (1<<i)
#         elif x: base |= (1<<i)
    
#     s = bitmask
#     while True:
#         t = base | s

#         if count_groups(t) == nongram[::-1]: cnt += 1
#         if s == 0: return cnt
#         s = (s-1)&bitmask
    
# s = 0
# from tqdm import tqdm
# for pattrn, nongram in tqdm(springs):
#     s += bruteforce(pattrn, nongram)

def is_valid_state(pattern, nonogram):
    
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def count_ways(pattern, nonogram):
    solutions = []
    state = set(pattern)
    search(state, solutions)
    return solutions
# print(s)