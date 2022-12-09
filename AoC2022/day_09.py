import aoc_helper
from aoc_helper import (
    range,
)

raw = aoc_helper.fetch(9, 2022)
#raw = open("sample_input.txt").read()

def parse_raw():
    return [(i.split()[0],int(i.split()[1])) for i in raw.splitlines()]


steps = parse_raw()

def sgn(x):return 1 if x > 0 else (-1 if x < 0 else 0)

def part_one():
    path_tail = set()
    xh,yh,xt,yt = 0,0,0,0
    for i in steps:
        for j in range(i[1]):
            xh += 1 if i[0] == 'R' else (-1 if i[0] == 'L' else 0)
            yh += 1 if i[0] == 'U' else (-1 if i[0] == 'D' else 0)
            while abs(xt-xh) > 1 or abs(yt-yh) > 1:
                path_tail.add((xt,yt))
                xt += sgn(xh-xt)
                yt += sgn(yh-yt)
                path_tail.add((xt,yt))
    print(len(path_tail))
    return len(path_tail)
                
                    
def part_two():
    path_tail = set()
    rope_x = [0]*10
    rope_y = [0]*10
    for i in steps:
        for j in range(i[1]):
            rope_x[0] += 1 if i[0] == 'R' else (-1 if i[0] == 'L' else 0)
            rope_y[0] += 1 if i[0] == 'U' else (-1 if i[0] == 'D' else 0)
            for k in range(1,9):
                while abs(rope_x[k]-rope_x[k-1]) > 1 or abs(rope_y[k]-rope_y[k-1]) > 1:
                    rope_x[k] += sgn(rope_x[k-1]-rope_x[k])
                    rope_y[k] += sgn(rope_y[k-1]-rope_y[k])
            k = 9
            while abs(rope_x[k]-rope_x[k-1]) > 1 or abs(rope_y[k]-rope_y[k-1]) > 1:
                path_tail.add((rope_x[-1],rope_y[-1]))
                rope_x[k] += sgn(rope_x[k-1]-rope_x[k])
                rope_y[k] += sgn(rope_y[k-1]-rope_y[k])
                path_tail.add((rope_x[-1],rope_y[-1]))
    return len(path_tail)
                    

aoc_helper.lazy_submit(day=9, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=9, year=2022, solution=part_two)
