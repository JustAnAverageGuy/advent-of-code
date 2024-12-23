from collections import defaultdict 

import aoc_helper

raw = aoc_helper.fetch(23, 2024)


def parse_raw(raw: str):
    nei = defaultdict(set)
    for i in raw.splitlines():
        a,b = i.split('-')
        nei[a].add(b)
        nei[b].add(a)
    return nei


data = parse_raw(raw)


def part_one(data=data):
    threcon = set()
    for a in data:
        if a[0] == "t":
            for b in data[a]:
                for x in (data[b] & data[a]): threcon.add(tuple(sorted((a,b,x))))
    return len(threcon)

import networkx
def part_two(data=data):
    g = networkx.Graph(data)
    s = max(networkx.find_cliques(g), key=len)
    return  ",".join(sorted(s))


aoc_helper.lazy_test(day=23, year=2024, parse=parse_raw, solution=part_one)

aoc_helper.lazy_test(day=23, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=23, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=23, year=2024, solution=part_two, data=data)
