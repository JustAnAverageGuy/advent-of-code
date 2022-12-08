import aoc_helper
from aoc_helper import (
    Grid,
    range,
)

raw = aoc_helper.fetch(8, 2022)


def parse_raw():
    return Grid.from_string(raw).data


grid = parse_raw()
r, c = len(grid), len(grid[0])


def part_one():
    mask = []
    for _ in range(r):
        mask.append([0]*c)
    cnt = 0
    for y in range(r):
        mx, my, m_x, m_y = -1, -1, -1, -1
        for x in range(c):  # same in this case as square grid
            if (grid[y][x] > mx):  # moving along x
                mx = grid[y][x]
                if (mask[y][x] == 0):
                    mask[y][x] = 1
                    cnt += 1
            if (grid[y][c-1-x] > m_x):
                m_x = grid[y][c-1-x]
                if (mask[y][c-1-x] == 0):
                    mask[y][c-1-x] = 1
                    cnt += 1
            if (grid[x][y] > my):  # moving along y
                my = grid[x][y]
                if (mask[x][y] == 0):
                    mask[x][y] = 1
                    cnt += 1
            if (grid[c-1-x][y] > m_y):
                m_y = grid[c-1-x][y]
                if (mask[c-1-x][y] == 0):
                    mask[c-1-x][y] = 1
                    cnt += 1
    return cnt


def scescr(y: int, x: int):
    sx = s_x = sy = s_y = 0
    h = grid[y][x]
    dx = dy = 1
    while ((x+dx) < c):
        sx += 1
        if (h <= grid[y][x+dx]):
            break
        dx += 1
    while ((y+dy) < r):
        sy += 1
        if (h <= grid[y+dy][x]):
            break
        dy += 1
    dx = dy = 1
    while ((x-dx) > -1):
        s_x += 1
        if (h <= grid[y][x-dx]):
            break
        dx += 1
    while ((y-dy) > -1):
        s_y += 1
        if (h <= grid[y-dy][x]):
            break
        dy += 1
    return sx*s_x*sy*s_y


def part_two():
    m = 0
    cor = (-1, -1)
    assert (scescr(0, 2) == 0) and (scescr(1, 2) == 16)
    for y in range(1, r-1):
        for x in range(1, c-1):
            if ((t := scescr(y, x)) > m):
                m = t
                cor = (y, x)
    print(m, cor)
    return m


aoc_helper.lazy_submit(day=8, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=8, year=2022, solution=part_two)
