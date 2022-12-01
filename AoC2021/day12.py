
with open("input12.txt", 'r') as file:
    edges = [i.strip().split('-') for i in file.readlines()]

with open("testinput.txt", 'r') as file:
    edges = [i.strip().split('-') for i in file.readlines()]


nodes = list(set(j for i in edges for j in i))

graph = dict()
for node in nodes:
    neighbours = []
    for edge in edges:
        if node in edge:
            neighbours.append(edge[1-edge.index(node)])
    graph[node] = neighbours

# Graph = {Node : [Neighbours]}


def delet(node: str, graph: dict[str, list[str]]):
    if node not in graph:
        return graph
    else:
        neigh = graph[node]
        for n in neigh:
            graph[n].remove(node)
        return graph


def noofpaths(graph: dict[str, list[str]], startingNode: str):
    if startingNode == 'end':
        return 1
    cnt = 0
    neighbours = graph[startingNode]
    modifiedGraph = delet(
        startingNode, graph) if startingNode.islower() else graph
    for neighbour in neighbours:
        cnt += noofpaths(modifiedGraph, neighbour)
    return cnt


print(noofpaths(graph, 'start'))
