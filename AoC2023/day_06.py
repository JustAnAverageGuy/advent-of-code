import aoc_helper
from aoc_helper import (
    extract_ints,
    map,
    range,
)

import sys


EXAMPLE = "EXAMPLE" in sys.argv
TWO = "2" in sys.argv

if EXAMPLE:
    if TWO:
        raw, answer = aoc_helper.get_sample_input(day=6, year=2023, part=2)
    else: 
        raw, answer = aoc_helper.get_sample_input(day=6, year=2023, part=1)
else:
    raw = aoc_helper.fetch(6, 2023)


times, distances =  raw.splitlines()
times = extract_ints(times)
distances = extract_ints(distances)

races = [*zip(times, distances)]

# part 1

p = 1

for t,d in races:
    c = 0
    for w in range(t):
        if (t-w)*w > d: c += 1
    p *= c
    
print(p)

# part 2

time = int("".join(map(str,times)))
distance = int("".join(map(str,distances)))

if (time*time)/4 < distance: print(0); exit()

def f(m,t=time, d=distance):
    return (t-m)*m > d

l = -1
r = (time//2) + 1

while (r-l) > 1:
    m = (l+r)//2
    if f(m):
        r = m
    else:
        l = m
print(time - 2*r + 1 )

# bruteforce takes ~28s
# c = 0
# for w in tqdm(range(time)):
#     c += (time-w)*w > distance
# print(c)