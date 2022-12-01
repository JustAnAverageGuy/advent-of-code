from functools import reduce
import numpy


def basin_lookup(index):
    x = ndarray[index]
    basin_array = [index]
    if ndarray.shape[1] != index[1] + 1 and ndarray[index[0], index[1]+1] > x and ndarray[index[0], index[1]+1] != 9:
        basin_array = basin_array + basin_lookup((index[0], index[1] + 1))
    if ndarray.shape[0] != index[0] + 1 and ndarray[index[0] + 1, index[1]] > x and ndarray[index[0] + 1, index[1]] != 9:
        basin_array = basin_array + basin_lookup((index[0] + 1, index[1]))
    if -1 != index[1] - 1 and ndarray[index[0], index[1] - 1] > x and ndarray[index[0], index[1] - 1] != 9:
        basin_array = basin_array + basin_lookup((index[0], index[1] - 1))
    if -1 != index[0] - 1 and ndarray[index[0] - 1, index[1]] > x and ndarray[index[0] - 1, index[1]] != 9:
        basin_array = basin_array + basin_lookup((index[0] - 1, index[1]))
    return basin_array


ndarray = numpy.genfromtxt('input.txt', delimiter=1, dtype=int)
count = 0
shape = ndarray.shape
basin_sizes = []
for index, x in numpy.ndenumerate(ndarray):
    if ndarray.shape[1] == index[1] + 1 or ndarray[index[0], index[1]+1] > x:
        if ndarray.shape[0] == index[0] + 1 or ndarray[index[0] + 1, index[1]] > x:
            if -1 == index[1] - 1 or ndarray[index[0], index[1] - 1] > x:
                if -1 == index[0] - 1 or ndarray[index[0] - 1, index[1]] > x:
                    basin_sizes.append(len(set(basin_lookup(index))))
                    count += 1 + x
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
print(count)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


with open("input9.txt", 'r') as file:
    G = [[int(k) for k in i.strip()]
         for i in file.readlines()]


def getNeighbors(G, i, j, includeCoordinates=False):
    neighbors = []
    # top
    if i > 0:
        if includeCoordinates:
            neighbors.append((G[i-1][j], (i-1, j)))
        else:
            neighbors.append(G[i-1][j])
    # bottom
    if i < len(G)-1:
        if includeCoordinates:
            neighbors.append((G[i+1][j], (i+1, j)))
        else:
            neighbors.append(G[i+1][j])
    # right
    if j < len(G[0])-1:
        if includeCoordinates:
            neighbors.append((G[i][j+1], (i, j+1)))
        else:
            neighbors.append(G[i][j+1])
    # left
    if j > 0:
        if includeCoordinates:
            neighbors.append((G[i][j-1], (i, j-1)))
        else:
            neighbors.append(G[i][j-1])
    return neighbors


def isLow(G, i, j):
    me = G[i][j]
    if me == 9:
        return False
    neighbors = sorted(getNeighbors(G, i, j))
    return me < neighbors[0]


def findLows(G, includeCoordinates=False):
    lows = []
    for row in range(len(G)):
        for col in range(len(G[0])):
            if isLow(G, row, col):
                if includeCoordinates:
                    lows.append((G[row][col], (row, col)))
                else:
                    lows.append(G[row][col])
    return lows


lows = findLows(G)
ANS1 = sum_risk_levels = sum(map(lambda x: x+1, lows))
lows_w_coords = findLows(G, True)
# BFS


def findBasin(G, i, j):
    basin = []
    queue = []
    me = G[i][j]
    basin.append((i, j))
    queue.append((i, j))
    while queue:
        s = queue.pop(0)
        neighbors_no_nines = list(
            filter(lambda x: x[0] < 9, getNeighbors(G, s[0], s[1], True)))
        for n in neighbors_no_nines:
            if n[1] not in basin:
                basin.append(n[1])
                queue.append(n[1])
    return basin


basins = []
for low_coord in lows_w_coords:
    basins.append(findBasin(G, low_coord[1][0], low_coord[1][1]))

ANS2 = reduce(lambda x, y: x * y,
              list(map(len, sorted(basins, key=len, reverse=True)[0:3])))
print("ans1={}".format(ANS1))  # 588
print("ans2={}".format(ANS2))  # 964712

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
