with open(r"AoC2019\AoC2019_Day3_input.txt", 'r') as f:
    W1 = f.readline().strip().split(',')
    W2 = f.readline().strip().split(',')


def locus(path):
    paths = []
    x, x1, y, y1 = 0, 0, 0, 0
    for i in path:
        if i[0] == 'R':
            x1 = x + int(i[1:])
        if i[0] == 'L':
            x1 = x - int(i[1:])
        if i[0] == 'D':
            y1 = y - int(i[1:])
        if i[0] == 'U':
            y1 = y + int(i[1:])
        [paths.append((a, b)) for a in range(x, x1+1) for b in range(y, y1+1)]
        x, y = x1, y1
    return paths


# print(locus(W1).intersection(locus(W2)))

# intersections = locus(W1).intersection(locus(W2)) # {(-4598, 4355), (-3370, 5598), (-1932, 3049), (-4769, 4355), (-3913, 5056), (-3913, 4983), (-2723, 3584), (-4216, 3653), (-4607, 5279), (-3471, 3826)}
intersections = [(-4598, 4355), (-3370, 5598), (-1932, 3049), (-4769, 4355), (-3913, 5056),
                 (-3913, 4983), (-2723, 3584), (-4216, 3653), (-4607, 5279), (-3471, 3826)]
p1 = locus(W1)
p2 = locus(W2)
print(sorted(intersections, key=lambda x: p1.index(x)+p2.index(x)))
print(p1.index((-3370, 5598))+p2.index((-3370, 5598)))
