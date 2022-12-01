""" import numpy as np


with open("input9.txt", 'r') as file:
    heights = np.array([[int(k) for k in i.strip()]
                       for i in file.readlines()], dtype=np.int16)


trench = np.full((len(heights) + 2, len(heights[0]) + 2), 10)

trench[1:-1, 1:-1] = heights
heightchanges = np.zeros_like(trench,dtype=np.int16)
p
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]]

for y in range(1,len(trench)-1):
    for x in range(1,len(trench[0])-1):
        differnces = []
        for i in range(4):

            

 
def isLow(heights, y, x):
    if x*y == 0 or y == len(heights)-1 or x == len(heights[0]) - 1:
        return False
    k = heights[y, x]
    islow = 1
    for i in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        islow &= (k < heights[y + i[0], x + i[1]])
        if not islow:
            return False
    return True

risk = 0
for i in range(1, len(trench) - 1):
    for j in range(1, len(trench[0]-1)):
        if isLow(trench, i, j):
            risk += trench[i, j] + 1
print(risk)
 """
with open("input9.txt", 'r') as file:
    heights = [[int(k) for k in i.strip()]
               for i in file.readlines()]

trench = [[10]*(len(heights) + 2)] + [[10] + i + [10]
                                      for i in heights] + [[10]*(len(heights) + 2)]

dirn = [(0, 1), (-1, 0), (0, -1), (1, 0)]

descents = [[-1]*len(trench[0]) for _ in range(len(trench))]

ans = 0

for y in range(1, len(trench) - 1):
    for x in range(1, len(trench[0]) - 1):
        k = trench[y][x]
        diff = []
        for i in range(4):
            diff.append(0 if k == trench[y+dirn[i][0]][x+dirn[i][1]]
                        else (-1 if k > trench[y+dirn[i][0]][x+dirn[i][1]] else 1))
        descents[y][x] == tuple(diff)
#        if diff == [1, 1, 1, 1]:
#            ans += trench[y][x] + 1

print(ans)
