import aoc_helper
from aoc_helper import (
    list,
    range,
)
import sys
from colorist import *

DAY = 11
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

x = raw.splitlines()

HEIGHT = len(x)
WIDTH  = len(x[0])

i = 0
while i < HEIGHT:
    if set(x[i]) == {'.'}:
        x.insert(i+1, '.'*WIDTH)
        i += 1
        HEIGHT += 1
    i += 1 

trans = ["".join(x[i][j] for i in range(HEIGHT)) for j in range(WIDTH)]

i = 0
while i < WIDTH:
    if set(trans[i]) == {'.'}:
        trans.insert(i+1, '.'*HEIGHT)
        i += 1
        WIDTH += 1
    i += 1

points = []

for i in range(WIDTH):
    for j in range(HEIGHT):
        if trans[i][j] == '#':
            points.append((i,j))

s = 0
dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
for i,x in enumerate(points):
    for j in points[i+1:]:
        s += dist(x,j)
        
print(f'Part 1: {BrightColor.CYAN}{s}{BrightColor.OFF}')

# PART 2:
rows = raw.splitlines()
HEIGHT = len(rows)
WIDTH  = len(rows[0])

vertical_offsets   = list([0]*HEIGHT)
horizontal_offsets = list([0]* WIDTH)

for i,x in enumerate(rows):
    if set(x) == {'.'}: vertical_offsets[i] += 1

for i,x in enumerate([[rows[i][j] for i in range(HEIGHT)] for j in range(WIDTH)]):
    if set(x) == {'.'}: horizontal_offsets[i] += 1

vertical_offsets   =   vertical_offsets.accumulated(lambda x,y:x+y)
horizontal_offsets = horizontal_offsets.accumulated(lambda x,y:x+y)
points = []

EXPANSION_FACTOR = 1_000_000 - 1
# EXPANSION_FACTOR = 9

for i in range(HEIGHT):
    for j in range(WIDTH):
        if rows[i][j] == '#': points.append((i + vertical_offsets[i]*EXPANSION_FACTOR,j + horizontal_offsets[j]*EXPANSION_FACTOR)) # y,x

s = 0
dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
for i,x in enumerate(points):
    for j in points[i+1:]:
        s += dist(x,j)
print(f'Part 2: {BrightColor.CYAN}{s}{BrightColor.OFF}')
