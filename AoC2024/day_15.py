import aoc_helper
from aoc_helper import (
    Grid,
    SparseGrid,
    list,
    range,
)

raw = aoc_helper.fetch(15, 2024)


def parse_raw(raw: str):
    a,b = raw.split("\n\n")
    g = Grid.from_string(a, classify=lambda x: {"#":1, ".":0, "O": 2, "@": 3}[x])
    steps = b.replace("\n","")
    return g, steps



data = parse_raw(raw)


def move(xy, dirn, grid:Grid):
    x,y = xy
    nx,ny = x + dirn[0], y + dirn[1]
    nxt = grid.get(nx, ny, 1)
    # print(xy, dirn, nxt)
    if nxt == 0:
        grid[ny][nx] = grid[y][x]
        grid[y][x] = 0
        return (True, (nx,ny))
    elif nxt == 1:
        return (False, xy)
    else:
        # nxt has to be 2 now
        assert nxt == 2
        ok, _ = move((nx,ny), dirn, grid)
        if not ok: return (False, xy)
        grid[ny][nx] = grid[y][x]
        grid[y][x] = 0
        return (True, (nx,ny))

def move2(xy, dirn, grid:Grid, simul:bool):
    x,y = xy
    nx,ny = x + dirn[0], y + dirn[1]
    nxt = grid.get(nx, ny, 1)
    if nxt == 0:
        if not simul:
            grid[ny][nx] = grid[y][x]
            grid[y][x] = 0
        return (True, (nx,ny))
    elif nxt == 1:
        return (False, xy)
    else:
        # nxt is one of 2 or 3 ( `[` or `]` )
        assert nxt in (2,3)
        if ny == y: # horizontal push
            ok, _ = move2((nx, ny), dirn, grid, simul)
            if not ok: return (False, xy)
            if not simul:
                grid[ny][nx] = grid[y][x]
                grid[y][x] = 0
            return (True, (nx,ny))
        
        # vertical push
        if nxt == 2: adj = (nx+1, ny)
        else: adj = (nx-1, ny)

        okl, _ = move2((nx, ny), dirn, grid, simul=True)
        if not okl: return (False, xy)
        okr, _ = move2(adj, dirn, grid, simul=True)
        if not okr: return (False, xy)
        move2((nx,ny), dirn, grid, simul)
        move2(adj, dirn, grid, simul)
        if not simul:
            grid[ny][nx] = grid[y][x]
            grid[y][x] = 0
        return (True, (nx,ny))
        



def part_one(data=data):
    x, steps = data

    grid = Grid(list([i.copy() for i in x]))

    H, W = grid.height, grid.width
    start = list(grid.find_all(SparseGrid.from_string("3", default_factory=int)))[0]
    dirns = {
        ">" : (1, 0),
        "<" : (-1, 0),
        "v" : (0, 1),
        "^" : (0, -1),
    }
    for d in steps:
        _, start = move(start, dirns[d], grid)
    tot = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 2:
                tot += 100*y+x
    return tot

aoc_helper.lazy_test(day=15, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    x, steps = data
    xx = list()
    for i in x:
        curr = list()
        # . -> 0
        # # -> 1
        # [ -> 2
        # ] -> 3
        # @ -> 4
        for j in i:
            if j == 0: curr.extend([0,0])
            elif j == 1: curr.extend([1,1])
            elif j == 2: curr.extend([2,3])
            elif j == 3: curr.extend([4,0])
        xx.append(curr)

    grid = Grid(xx)

    H, W = grid.height, grid.width
    start = list(grid.find_all(SparseGrid.from_string("4", default_factory=int)))[0]
    dirns = {
        ">" : (1, 0),
        "<" : (-1, 0),
        "v" : (0, 1),
        "^" : (0, -1),
    }


    # print(grid)
    for d in steps:
        _, start = move2(start, dirns[d], grid, False)
        # print(f'Move {d}:')
        # print(grid)
        # ```bash
        #    py day_15.py | tr -d ' Grid()[]' | tr '01234' '.#[]@'
        # ```
    tot = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 2:
                tot += 100*y+x
    return tot

aoc_helper.lazy_test(day=15, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=15, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=15, year=2024, solution=part_two, data=data)
