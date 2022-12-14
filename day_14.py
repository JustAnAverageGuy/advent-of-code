import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)

raw = aoc_helper.fetch(14, 2022)

def parse_raw():
    return [list(map(lambda x: tuple(map(int,x.split(','))),i.split(' -> '))) for i in raw.splitlines()]


data = parse_raw()

cave_structure = set()
y_max = 0
for i in data:
    for k in range(len(i)-1):
        if i[k][0] == i[k+1][0]:
            for y in irange(i[k][1],i[k+1][1]):cave_structure.add((i[k][0],y))
        else:
            assert(i[k][1] == i[k+1][1])
            for x in irange(i[k][0],i[k+1][0]):cave_structure.add((x,i[k][1]))
        y_max = max(y_max,i[k][1])
    y_max = max(y_max,i[-1][1])
    
# Alternatively rather than storing all 700 or so rock points, since they are horizontal and vertical, we can also store the y coordinates and the range of x and similarly ofr x, to check for "barriers"
# but adding sand points is a bit easier this way ig

def part_one():
    sand_count = 0
    occupied = cave_structure.copy()
    while True:
        x,y = 500,0 # source = 500,0
        while True:
            if y >= y_max: return sand_count
            if((x,y +1) not in occupied):
                y += 1
            elif( (x-1,y+1) not in occupied):
                x -= 1
                y += 1
            elif( (x+1,y+1) not in occupied ):
                x += 1
                y += 1
            else:
                sand_count += 1
                occupied.add((x,y))
                break
        


def part_two():
    floor  = 2 + y_max
    sand_count = 0
    occupied = cave_structure.copy()
    while True:
        x,y = 500,0 # source = 500,0
        while True:
            if((x,y +1) not in occupied and y+1 < floor):
                y += 1
            elif( (x-1,y+1) not in occupied and (y+1 < floor)):
                x -= 1
                y += 1
            elif( (x+1,y+1) not in occupied and (y+1 < floor)):
                x += 1
                y += 1
            else:
                if y == 0: return sand_count + 1
                sand_count += 1
                occupied.add((x,y))
                break


aoc_helper.lazy_submit(day=14, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=14, year=2022, solution=part_two)
