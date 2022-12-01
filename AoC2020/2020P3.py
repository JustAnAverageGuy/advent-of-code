with open("AoC2020_Day3_input.txt", 'r') as file:
    forest = list(map(lambda x: x.strip(), file.readlines()))

""" with open("input.txt", 'r') as file:
    smallForest = list(map(lambda x: x.strip(), file.readlines()))
 """

""" def treesonslope(right, down, hill):
    cnt = 0
    for i in range(0, len(hill), down):
        if hill[i][((right*i)//down) % len(hill[0])] == r'#':
            cnt += 1
    return cnt
 """

# BOTH OF THESE IMPLEMENTATIONS WORK AFAIK


def treesonslope(right, down, hill):
    cnt = 0
    length, depth = 0, 0
    while depth < len(hill):
        if hill[depth][length % len(hill[0])] == r'#':
            cnt += 1
        depth += down
        length += right
    return cnt


prod = 1
for i in [1, 3, 5, 7]:
    prod *= treesonslope(i, 1, forest)

print(prod * treesonslope(1, 2, forest))
