with open("input5.txt", 'r') as file:
    poin = [[tuple(map(int, j.split(',')))
             for j in i.strip().split(' -> ')] for i in file.readlines()]


goodpointsVertical = [sorted(i, key=lambda x:x[1])
                      for i in poin if (i[0][0] == i[1][0])]

goodpointsHorizontal = [sorted(i, key=lambda x:x[0])
                        for i in poin if (i[0][1] == i[1][1])]

goodpointsPositiveDiagonal = [sorted(i, key=lambda x:x[0]) for i in poin if (
    i[1][1] + i[0][0] == i[1][0]+i[0][1])]

goodpointsNegativeDiagonal = [sorted(i, key=lambda x:x[0]) for i in poin if (
    i[0][0] + i[0][1] == i[1][0] + i[1][1])]

# print(goodpointsNegativeDiagonal)

visitedpoints = dict()


def addindict(dic, point):
    if point in dic:
        dic[point] += 1
    else:
        dic[point] = 1
    return dic


for i in goodpointsVertical:
    for j in range(i[0][1], i[1][1]+1):
        visitedpoints = addindict(visitedpoints, (i[0][0], j))

for i in goodpointsHorizontal:
    for j in range(i[0][0], i[1][0]+1):
        visitedpoints = addindict(visitedpoints, (j, i[0][1]))

for i in goodpointsPositiveDiagonal:
    for x in range(i[0][0], i[1][0]+1):
        visitedpoints = addindict(visitedpoints, (x, i[0][1]-i[0][0] + x))

for i in goodpointsNegativeDiagonal:
    for x in range(i[0][0], i[1][0]+1):
        visitedpoints = addindict(visitedpoints, (x, i[0][0] + i[0][1] - x))


cnt = 0
for k in visitedpoints:
    if visitedpoints[k] > 1:
        cnt += 1
print(cnt)
# print(max(visitedpoints.values()))
