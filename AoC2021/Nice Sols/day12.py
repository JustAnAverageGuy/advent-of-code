import re

caves = {}


def get_input():
    with open("input12.txt") as f:
        while True:
            line = f.readline()
            if line == "":
                break

            connection = re.findall(r"(\w+)-(\w+)", line)[0]

            try:
                caves[connection[0]].append(connection[1])
            except:
                caves[connection[0]] = [connection[1]]

            try:
                caves[connection[1]].append(connection[0])
            except:
                caves[connection[1]] = [connection[0]]


def backtrack(current_cave=None, visited_caves=None, has_double_visited=False):
    if current_cave == "end":
        return 1

    if current_cave is None or visited_caves is None:
        current_cave = "start"
        visited_caves = []

    paths = 0
    visited_caves.append(current_cave)

    for adjacent_cave in caves[current_cave]:
        if adjacent_cave == "start":
            continue
        if adjacent_cave.isupper():
            paths += backtrack(adjacent_cave, visited_caves,
                               has_double_visited)

        elif adjacent_cave not in visited_caves:
            paths += backtrack(adjacent_cave, visited_caves,
                               has_double_visited)
        elif not has_double_visited:
            paths += backtrack(adjacent_cave, visited_caves, True)

    visited_caves.remove(current_cave)

    return paths


get_input()
print(backtrack())
print(caves)
