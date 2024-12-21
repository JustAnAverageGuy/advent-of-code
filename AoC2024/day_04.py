import aoc_helper

raw = aoc_helper.fetch(4, 2024)

def parse_raw(raw: str):
    return raw.splitlines()

data = parse_raw(raw)

def part_one(data=data):
    s = 0
    for i in data: s += i.count("XMAS")
    for i in data: s += i.count("XMAS"[::-1])
    trans = [
     "".join([data[i][j] for i in range(len(data))]) for j in range(len(data[0]))
    ]
    for i in trans: s += i.count("XMAS")
    for i in trans: s += i.count("XMAS"[::-1])

    diagonals = []

    w = len(data[0])
    h = len(data)

    for sm in range(w+h-1):
        cur = []
        for y in range(0,sm+1):
            x = sm - y
            if 0 <= y < h and 0 <=x < w: cur.append(data[y][x])
        diagonals.append("".join(cur))

    other_diag = []
    for dif in range(-(w-1), h):
        cur = []
        for x in range(w):
            y = x + dif
            if 0 <= y < h and 0 <=x < w: cur.append(data[y][x])
        other_diag.append("".join(cur))
        

    for i in diagonals:
        s += i.count("XMAS")
        s += i.count("XMAS"[::-1])

    for i in other_diag:
        s += i.count("XMAS")
        s += i.count("XMAS"[::-1])
    return s


aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_one)

def part_two(data=data):
    s = 0
    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            if data[y][x] == "A":
                if {data[y-1][x-1], data[y+1][x+1]} == {"M", "S"} == {data[y-1][x+1], data[y+1][x-1]}: s += 1
    return s


aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2024, solution=part_two, data=data)
