from collections import defaultdict

import aoc_helper

raw = aoc_helper.fetch(11, 2025)


def parse_raw(raw: str):
    graph = {}
    for line in raw.splitlines():
        a, *b = line.split()
        graph[a.strip()[:-1]] = b
    return graph


data = parse_raw(raw)


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    nodes = set()
    for node in graph:
        nodes.add(node)
        for child in graph[node]:
            nodes.add(child)
    nodes = list(nodes)
    node_pos = {s: i for i, s in enumerate(nodes)}
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[nodes[node]]

    # cycle check
    for node in res:
        if any(found[node_pos[nei]] for nei in graph[node]):
            # return None
            return []
        found[node] = 0

    return res[::-1]


def part_one(data=data):
    # assuming acyclicity, because otherwise its infinte
    reversed_graph = defaultdict(list)
    for a, b in data.items():
        for x in b:
            # reversed_graph[x].append(a)
            reversed_graph[x].append(a)

    ctr = defaultdict(int)
    ctr["out"] = 1

    for node in topological_sort(reversed_graph):
        for child in reversed_graph[node]:
            ctr[child] += ctr[node]
    return ctr["you"]


aoc_helper.lazy_test(day=11, year=2025, parse=parse_raw, solution=part_one)


def count_paths_from_starts_to_end(reversed_graph, starts: list[str], end):
    ctr = defaultdict(int)
    ctr[end] = 1

    for node in topological_sort(reversed_graph):
        for child in reversed_graph[node]:
            ctr[child] += ctr[node]

    return {start: ctr.get(start, 0) for start in starts}


def part_two(data=data):
    reversed_graph = defaultdict(list)
    for a, b in data.items():
        for x in b:
            reversed_graph[x].append(a)

    cnts = count_paths_from_starts_to_end(reversed_graph, ["dac", "fft"], "out")

    dac_out = cnts["dac"]
    fft_out = cnts["fft"]

    cnts = count_paths_from_starts_to_end(reversed_graph, ["svr", "fft"], "dac")

    fft_dac = cnts["fft"]
    svr_dac = cnts["svr"]

    cnts = count_paths_from_starts_to_end(reversed_graph, ["svr", "dac"], "fft")

    svr_fft = cnts["svr"]
    dac_fft = cnts["dac"]

    return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out


aoc_helper.lazy_test(day=11, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2025, solution=part_two, data=data)
