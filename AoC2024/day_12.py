from collections import Counter, defaultdict, deque

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
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(12, 2024)


def parse_raw(raw: str):
    return Grid.from_string(raw, classify=lambda x: x)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

from tqdm import tqdm

def part_one(data=data):
    w,h = len(data[0]), len(data.data)
    visited = [[False]*w for _ in range(h)]
    tot = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x]: continue
            area = 0
            peri = 0
            stk = [(x,y)]
            while stk:
                nx, ny = stk.pop()
                if visited[ny][nx]: continue
                visited[ny][nx] = True
                area += 1
                peri += 4
                for pxy,nv in data.orthogonal_neighbours(nx, ny):
                    if nv == data[ny][nx]:
                        peri -= 1
                        stk.append(pxy)
            tot += area * peri
    return tot
    


aoc_helper.lazy_test(day=12, year=2024, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)

def part_two(data=data):
    w,h = len(data[0]), len(data.data)
    visited = [[False]*w for _ in range(h)]
    tot = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x]: continue
            area = 0
            sides = [set(), set()]
            stk = [(x,y)]
            while stk:
                nx, ny = stk.pop()
                if visited[ny][nx]: continue
                visited[ny][nx] = True
                area += 1

                edges = [
                    (nx,ny,nx+1,ny),
                    (nx,ny+1,nx+1,ny+1),
                    (nx,ny,nx,ny+1),
                    (nx+1,ny,nx+1,ny+1),
                ]

                for i, edge in enumerate(edges):
                    ishor = (i < 2)
                    isin = i % 2
                    complement = (*edge, 1 - isin)
                    if complement in sides[ishor]:
                        sides[ishor].remove(complement)
                        continue
                    sides[ishor].add((*edge, isin))

                for pxy,nv in data.orthogonal_neighbours(nx, ny):
                    if nv == data[ny][nx]:
                        stk.append(pxy)

            # colesce individual edges on same side 

            horizontal_edges = sorted(sides[1], key= lambda x: (x[1], x[0], x[2]))

            coalesce_hori = []
            for cx, cy, cxn, _, typ in horizontal_edges:
                if (not coalesce_hori) or (coalesce_hori[-1][2] != cy) or (coalesce_hori[-1][3] != typ) or (coalesce_hori[-1][1] < cx):
                    coalesce_hori.append((cx, cxn, cy, typ))
                else:
                    coalesce_hori[-1] = (coalesce_hori[-1][0], max(coalesce_hori[-1][1], cxn) ,cy, typ)


            vertical_edges = sorted(sides[0], key= lambda x: (x[0], x[1], x[3]))

            coalesce_vert = []
            for cx, cy, _, cyn, typ in vertical_edges:
                if (not coalesce_vert) or (coalesce_vert[-1][2] != cx) or (coalesce_vert[-1][3] != typ) or (coalesce_vert[-1][1] < cy):
                    coalesce_vert.append((cy, cyn, cx, typ))
                else:
                    coalesce_vert[-1] = (coalesce_vert[-1][1], max(coalesce_vert[-1][1], cyn) ,cx, typ)

            tot += area * (len(coalesce_hori) + len(coalesce_vert))
    return tot


aoc_helper.lazy_test(day=12, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2024, solution=part_two, data=data)
