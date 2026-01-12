from collections import Counter, defaultdict, deque
from pprint import pprint

import aoc_helper

raw = aoc_helper.fetch(12, 2025)


def parse_raw(raw: str):
    *pieces, region_lines = raw.split("\n\n")
    shapes = [[[(c == "#") for c in line] for line in piece.splitlines()[1:]]  for piece in pieces  ]
    regions = []
    for line in region_lines.splitlines():
        sizes, countss = line.split(':')
        W,H = map(int,sizes.strip().split('x'))
        counts = list(map(int,countss.strip().split()))
        regions.append(((W,H), counts))
    return shapes, regions


data = parse_raw(raw)

def print_grid(data):
    for ro in data:
        print(*("⬜⬛"[i] for i in ro), sep="")


def area(piece):
    return sum(sum(i) for i in piece)

def part_one(data=data):
    # for piece in data[0]:
    #     print_grid(piece)
    #     print(area(piece))
    pieces = data[0]
    piece_areas = [area(i) for i in pieces]
    ans = 0
    for grid_sz, req in data[1]:
        area_available = grid_sz[0]*grid_sz[1]
        area_pieces = sum( i*j for i,j in zip(piece_areas, req) )
        # area_pieces = 9 * sum(req)
        # print(area_available, area_pieces, area_available > area_pieces)
        ans += area_available > area_pieces
    return ans



# aoc_helper.lazy_test(day=12, year=2025, parse=parse_raw, solution=part_one)


def part_two(data=data): ...


aoc_helper.lazy_test(day=12, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2025, solution=part_two, data=data)
