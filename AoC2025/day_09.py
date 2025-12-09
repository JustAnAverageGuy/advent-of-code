from itertools import combinations

import aoc_helper

raw = aoc_helper.fetch(9, 2025)


def parse_raw(raw: str):
    return [tuple(map(int, line.split(','))) for line in raw.splitlines()]


data = parse_raw(raw)

def part_one(data=data):
    return max((abs(x-a)+1)*(abs(y-b)+1)  for (x,y),(a,b) in combinations(data,2))


aoc_helper.lazy_test(day=9, year=2025, parse=parse_raw, solution=part_one)

def print_grid(grid):
    for row in grid:
        print(*("⬜⬛"[i] for i in row),sep="")


def part_two(data=data):
    edges = [(a,b) for a,b in zip(data, data[1:]+[data[0]])]

    xs_t = set()
    ys_t = set()

    for x,y in data:
        xs_t.add(x)
        ys_t.add(y)
    xs = sorted(xs_t)
    ys = sorted(ys_t)

    inv_x_map = { j: i for i,j in enumerate(xs) }
    inv_y_map = { j: i for i,j in enumerate(ys) }

    ans = 0
    H,W = len(ys), len(xs)

    grid = [ [0]* W for _ in range(H)]
    horizontal_edges = [tuple(sorted(edge)) for edge in edges if edge[0][1] == edge[1][1]]
    vertical_edges = [tuple(sorted(edge)) for edge in edges if edge[0][0] == edge[1][0]]
    horizontal_edges.sort(key=lambda x: (x[1],x[0]))
    vertical_edges.sort()
    
    # # print(xs, ys)
    # #### how to handle horizontal edges ????

    for i in range(H):
        is_inside = False
        for j in range(W):
            orig_x, orig_y = xs[j],ys[i]
            is_on_vertical_edge = any(
                (orig_x==x1) and y1 <= orig_y < y2 for ((x1,y1),(x2,y2)) in vertical_edges
                ##### less fking goooooooooooooo
                #### love you so much https://stackoverflow.com/a/78853954
            )
            if is_on_vertical_edge:
                # print(j,i,orig_x,orig_y,"on edge")
                grid[i][j] = 1
                is_inside = not is_inside
            if is_inside:
                grid[i][j] = 1

    # ## fill boundary only{{{
    # for (x1,y1), (x2,y2) in edges:
    #     i1,j1 = inv_x_map[x1], inv_y_map[y1]
    #     i2,j2 = inv_x_map[x2], inv_y_map[y2]
    #     if i1 == i2:
    #         for j in range(min(j1, j2), max(j1,j2)+1): grid[j][i1] = 1
    #     else:
    #         for i in range(min(i1, i2), max(i1,i2)+1): grid[j1][i] = 1
    # # }}}

    ## fill horizontal edges only{{{
    for (x1,y1), (x2,y2) in horizontal_edges:
        i1,j1 = inv_x_map[x1], inv_y_map[y1]
        i2,j2 = inv_x_map[x2], inv_y_map[y2]
        if i1 == i2:
            for j in range(min(j1, j2), max(j1,j2)+1): grid[j][i1] = 1
        else:
            for i in range(min(i1, i2), max(i1,i2)+1): grid[j1][i] = 1
    # }}}


    # print_grid(grid)
    # for ro in grid: print(*ro)
    for (x1,y1),(x2,y2) in combinations(data,2):
        j1,i1 = inv_x_map[x1], inv_y_map[y1]
        j2,i2 = inv_x_map[x2], inv_y_map[y2]
        i1, i2 = min(i1,i2), max(i1, i2)
        j1, j2 = min(j1,j2), max(j1, j2)
        # print((x1,y1),(x2,y2),'-',(j1,i1),(j2,i2))
        if not all( grid[i][j] for i in range(i1, i2+1) for j in range(j1, j2+1) ):
            # print("not OK")
            continue
        # print("OK")
        ans = max(ans, (abs(x1-x2)+1)*(abs(y1-y2)+1))
    return ans





#
aoc_helper.lazy_test(day=9, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2025, solution=part_two, data=data)
