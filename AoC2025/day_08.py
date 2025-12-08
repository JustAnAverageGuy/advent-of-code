from math import hypot, prod

import aoc_helper

raw = aoc_helper.fetch(8, 2025)


def parse_raw(raw: str):
    return [tuple(map(int,line.strip().split(','))) for line in raw.splitlines()]


data = parse_raw(raw)

class DSU:
    def __init__(self, nodes: list[tuple[int,int,int]]) -> None:
        n = len(nodes)
        self.parents = [i for i in range(n)]
        self.sizes = [1]*n
        self.circuit_lens = [0]*n
        self.nodes = nodes
        self.comp_sizes = n
    def parent(self, node):
        while self.parents[node] != node:
            self.parents[node] = node = self.parents[self.parents[node]]
        return node
    def union(self, a, b):
        pa, pb = self.parent(a), self.parent(b)
        if pa == pb: return self.comp_sizes
        if self.sizes[pa] < self.sizes[pb]: pa,pb = pb,pa
        self.parents[pb] = pa
        self.sizes[pa] += self.sizes[pb]
        self.comp_sizes -= 1
        return self.comp_sizes

        # edge_len = hypot(*(x-y for x,y in zip(self.nodes[a], self.nodes[b])))
    def get_leaders(self):
        return [i for i in range(len(self.parents)) if self.parent(i) == i]



def part_one(data=data):
    pq = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            dist = hypot(*(x-y for x,y in zip(data[i], data[j])))
            # heapq.heappush(pq, dist)
            pq.append((dist, i,j))
    pq.sort()
    # print(pq)
    dsu = DSU(data)
    for _,i,j in pq[:1000 if len(data) > 20 else 10]:
        # print(f'union: {data[i]} {data[j]}')
        dsu.union(i,j)
    circuit_sizes = [
        dsu.sizes[j] for j in dsu.get_leaders()
    ]
    circuit_sizes.sort(reverse=True)
    # print(circuit_sizes)
    return prod(circuit_sizes[:3])




aoc_helper.lazy_test(day=8, year=2025, parse=parse_raw, solution=part_one)

def part_two(data=data):
    pq = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            dist = hypot(*(x-y for x,y in zip(data[i], data[j])))
            # heapq.heappush(pq, dist)
            pq.append((dist, i,j))
    pq.sort()
    # print(pq)
    dsu = DSU(data)
    for _,i,j in pq:
        # print(f'union: {data[i]} {data[j]}')
        comp_size = dsu.union(i,j)
        if comp_size != 1: continue
        return data[i][0] * data[j][0]


aoc_helper.lazy_test(day=8, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2025, solution=part_two, data=data)
