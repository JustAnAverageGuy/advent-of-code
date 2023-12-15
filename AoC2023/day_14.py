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

DAY = 14
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


hmm = Grid.from_string(raw, classify=lambda x: ".#O".index(x))

SPACE = 0
ROCK = 1
BOULDER = 2


h = len(hmm.data)
w = len(hmm.data[0])

def find_north_load(hmm, ROCK, BOULDER):
    load = 0
    h = len(hmm.data)
    for col in (hmm.transpose()):
        stops = {-1: 0}
        last_rock = -1
        for j,x in enumerate(col):
            if x == BOULDER:
                stops[last_rock] += 1
            elif x == ROCK:
                last_rock = j
                stops[last_rock] = 0
        for rock, count in stops.items():
            load += (h-rock)*count - (count*(count+1))//2

    print(load)

find_north_load(hmm, ROCK, BOULDER, h)