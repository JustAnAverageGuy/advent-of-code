import aoc_helper
from aoc_helper import (
    Grid,
    range,
)

import sys

DAY = 10
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

G = Grid.from_string(raw, classify=lambda x: x)
n = len(G.data)

def nexs(x,y):
    hmm = G[y][x]
    check = [False]*4 # left right top bottom
    match hmm:
        case '.': return []
        case 'S': check       = [True]*4
        case '|': check[2:]   = [True]*2
        case '-': check[:2]   = [True]*2
        case 'L': check[1:3]  = [True]*2
        case 'J': check[0::2] = [True]*2
        case '7': check[0::3] = [True]*2
        case 'F': check[1::2] = [True]*2
        case _: assert False, f"Unknown character"
    neighbours = []
    if check[0] and x > 0   and G[y][x-1] in "-LFS": neighbours.append((x-1,y))
    if check[1] and x < n-1 and G[y][x+1] in "-J7S": neighbours.append((x+1,y))
    if check[2] and y > 0   and G[y-1][x] in "|7FS": neighbours.append((x,y-1))
    if check[3] and y < n-1 and G[y+1][x] in "|LJS": neighbours.append((x,y+1))
    return neighbours

for ys in range(n):
    for xs in range(n):
        if G[ys][xs] == 'S': break
    else:
        continue
    break

start = (xs,ys)

stk = [(start,None)]

retrace = dict()



while stk:
    curr, prev = stk.pop()
    if curr == start and prev is not None: break
    for nigh in nexs(*curr):
        if nigh == prev: continue
        stk.append((nigh, curr))
        retrace[nigh] = curr

path = [start]
while True:
    x = retrace[path[-1]]
    if x == start: break
    path.append(x)

print(f'Part 1:',len(path)//2)


# shoelace formula and picks theorem !

shoelace = path + [path[0]]

area = 0
for a,b in zip(shoelace, shoelace[1:]): area += (a[0]*b[1]) - (a[1]*b[0])

print(f'Part 2:',area/2 - len(path)/2 +1)