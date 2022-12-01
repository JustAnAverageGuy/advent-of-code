with open("input13.txt", 'r') as file:
    b = file.readlines()
    points = [tuple(map(int, i.strip().split(',')))
              for i in b if (i[0] != 'f' and i != '\n')]
    folds = [(i[11], int(i[13:].strip()))
             for i in b if i[0] == 'f']


def foldAlongfold(Points, fold):
    final = set()
    axis = 0 if fold[0] == 'x' else 1
    loc = fold[1]
    for i in Points:
        if i[axis] < loc:
            final.add(i)
        else:
            final.add((i[0], 2*loc - i[1]) if axis else (2*loc - i[0], i[1]))
    return final


point = points


with open('output.txt', 'w') as file:
    for i in folds:
        file.write('l'+str(folds.index(i)) + '= {')
        point = list(foldAlongfold(point, i))
        for j in point:
            file.write(str(j)+',')
        file.write('}\n')
# Export it to geogebra or something
