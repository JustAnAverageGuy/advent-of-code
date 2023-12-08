from collections import defaultdict
import re
import colorist as cl
import aoc_helper
from aoc_helper import (
    extract_ints,
    list,
)

raw = aoc_helper.fetch(2, 2023)

def pprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def extract_rgb(s):
    s = s.split(',')
    red, green, blue = 0,0,0
    for i in s:
        k = extract_ints(i)[0]
        if "red" in i: red = k
        if "green" in i: green = k
        if "blue" in i: blue = k
    return (red, green, blue)

import time, sys

delay = "DELAY" in sys.argv

def parse_raw(raw):
    games = defaultdict(list)
    for i in raw.splitlines():
        j = i.split(':')
        print(j[0], end=':')
        matches = re.finditer(r'(\d+) (red|green|blue)', j[1])
        red_starts = set()
        blu_starts = set()
        grn_starts = set()
        ends = set()
        for ma in matches:
            start, end = ma.span()
            col = ma.group(2)
            if col == "red": red_starts.add(start)
            elif col == "green": grn_starts.add(start)
            elif col == "blue": blu_starts.add(start)
            ends.add(end)
            # print(start, end, repr(col))
        
        for i, k in enumerate(j[1]):
            if i in red_starts: print(cl.BrightColor.RED,end='')
            if i in grn_starts: print(cl.BrightColor.GREEN,end='')
            if i in blu_starts: print(cl.BrightColor.BLUE,end='')
            if i in ends: print(cl.BrightColor.OFF,end='')
            pprint(k,end='')
            if delay: time.sleep(0.01)
            if k == ';': print('\n'+' '*8,end='')
        print(cl.BrightColor.OFF)
    return games


try:
    data = parse_raw(raw)
except KeyboardInterrupt:
    print(cl.BrightColor.OFF,cl.Color.OFF)
    cl.bright_yellow("******\n*DEAD*\n******")



def part_one(data):
    sid = 0
    for id, game in data.items():
        if all((j[0]<= 12 and j[1]<= 13 and j[2] <= 14) for j in game):
            sid += id
    return sid


def part_two(data):
    spow = 0
    for id, game in data.items():
        min_r = 0
        min_g = 0
        min_b = 0
        for k in game:
            min_r = max(min_r, k[0])
            min_g = max(min_g, k[1])
            min_b = max(min_b, k[2])
        spow += min_r*min_g*min_b
    return spow

