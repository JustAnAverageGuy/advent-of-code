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

DAY = 15
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


seq = raw.split(',')


def hash(s, p=17, m=256):
    s = [ord(i) for i in s]
    ini = 0
    for i in s:
        ini += i
        ini *= p
        ini %= m
    return ini


print(f"Part 1: {sum(map(hash, seq))}")

hashmap = {i: dict() for i in range(256)}

# hashmap = dict[ dict["string" : List[index, focus]] ]
filter_seq = []
remoable = set()
for i in seq[::-1]:
    if '-' in i:
        remoable.add(i[:-1])
    else:
        if i.split('=')[0] not in remoable:
            filter_seq.append(i)

seq = filter_seq[::-1]

# print(seq)

for i in seq:
    val, fous = i.split('=')
    fous = int(fous)
    idx = hash(val)
    if val in hashmap[idx]:
        hashmap[idx][val][1] = fous
    else:
        hashmap[idx][val] = [len(hashmap[idx])+1, fous]

# print(hashmap)
s = 0
for hash, box in hashmap.items():
    s += (hash+1) * sum(j[0]*j[1] for j in box.values())

print(s)
