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
    range,
    tail_call,
)

raw = aoc_helper.fetch(3, 2023)


def parse_raw(raw): return Grid.from_string(raw.strip(), classify=lambda x: x)


data = parse_raw(raw)

def part_one(data:Grid):
    n = len(data.data)
    symbol_locs = set()
    symbol_neighbours = set()
    for row in range(n):
        for column in range(n):
            if data[row][column] != '.' and not data[row][column].isdigit():
                symbol_locs.add((row, column))
                nei = data.neighbours(column, row)
                for loc, sym in nei:
                    if sym.isdigit(): symbol_neighbours.add(loc[::-1])
    already_handled = set()
    def extract_total_int(loc):
        nonlocal already_handled
        nonlocal data
        l = r = loc[1]
        row = loc[0]
        already_handled.add(loc)
        l -= 1
        r += 1
        while True:
            if l < 0: break
            if  data[row][l].isdigit():
                if (row, l) in already_handled: return False
                already_handled.add((row,l))
                l -= 1
            else:
                break
        while True:
            if r >= len(data.data[0]): break
            if  data[row][r].isdigit():
                if (row, r) in already_handled: return False
                already_handled.add((row,r))
                r += 1
            else:
                break
                
        return int("".join(data[row][l+1:r]))
    sm = 0
    for loc in symbol_neighbours:
        k = extract_total_int(loc)
        # if k : print(k)
        sm += k
    return sm

# aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(
    day=3,year=2023,solution=part_one,parse=parse_raw,
    test_data=
(
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""",4361)
)


def part_two(data):
    n = len(data.data)
    symbol_locs = dict()
    symbol_neighbours = set()
    for row in range(n):
        for column in range(n):
            if data[row][column] == '*':
                symbol_locs[(row, column)] = []
                nei = data.neighbours(column, row)
                for loc, sym in nei:
                    if sym.isdigit(): symbol_locs[(row, column)].append(loc[::-1])
    already_handled = set()
    def extract_total_int(loc):
        nonlocal already_handled
        nonlocal data
        l = r = loc[1]
        row = loc[0]
        already_handled.add(loc)
        l -= 1
        r += 1
        while True:
            if l < 0: break
            if  data[row][l].isdigit():
                if (row, l) in already_handled: return False
                already_handled.add((row,l))
                l -= 1
            else:
                break
        while True:
            if r >= len(data.data[0]): break
            if  data[row][r].isdigit():
                if (row, r) in already_handled: return False
                already_handled.add((row,r))
                r += 1
            else:
                break
                
        return int("".join(data[row][l+1:r]))
    sm = 0
    for loc in symbol_locs:
        neis = symbol_locs[loc]
        # print(neis)
        neints = []
        for j in neis:
            k = extract_total_int(j)
            if k : neints.append(k)
        if len(neints) == 2: 
            sm += neints[0]* neints[1]
    return sm


# aoc_helper.lazy_test(day=3, year=2023, parse=parse_raw, solution=part_two)
aoc_helper.lazy_test(
    day=3,year=2023,solution=part_two,parse=parse_raw,
    test_data=
(
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""",467835)
)

aoc_helper.lazy_submit(day=3, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2023, solution=part_two, data=data)
