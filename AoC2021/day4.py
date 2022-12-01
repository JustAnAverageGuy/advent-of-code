with open("input4.txt", 'r') as file:
    numbers = list(map(int, file.readline().strip().split(',')))
    gridsMarked = [(list(map(int, i.strip().split())), [[0, 0, 0, 0, 0] for _ in range(5)])
                   for i in file.read().split('\n\n')]

# print(gridsMarked[1])


def mark(gridMarked, number):
    grid, marked = gridMarked
    try:
        q = grid.index(number)
        marked[q//5][q % 5] = 1
        return (grid, marked)
    except ValueError:
        return (grid, marked)


""" def check(markd):
    ro = 1
    colmn = 1
    for i in range(5):
        for j in range(5):
            ro &= markd[i][j]
            colmn &= markd[j][i]
        if ro or colmn:
            return True
    return False """


def check(marked):
    for i in range(5):
        ro = 1
        colmn = 1
        for j in range(5):
            ro *= marked[i][j]
            colmn *= marked[j][i]
        if ro or colmn:
            return True


def winn(gridsm, numbs):
    for i in numbs:
        gridsm = [mark(j, i) for j in gridsm]
        for k in gridsm:
            if check(k[1]):
                print(gridsm.pop(gridsm.index(k)), i)


print(winn(gridsMarked, numbers))


""" def reshape(marked):
    new = ''
    for i in range(5):
        for j in range(5):
            new += marked[i*5 + j]+' '
        new += '\n'
    return new """


# IT WORED !!!
