with open("input8.txt", 'r') as file:
    display = [tuple(map(lambda x: x.strip().split(), i.strip().split(' | ')))
               for i in file.readlines()]

# print(display[0])
""" cnt = 0
for i in display:
    for j in i[1]:
        cnt += (len(j) in [2, 4, 3, 7])

print(cnt) """

sortedDisplay = [(sorted(list(map(lambda x: ''.join(sorted(x)), i[0])), key=len), list(
    map(lambda x: ''.join(sorted(x)), i[1]))) for i in display]

print(sortedDisplay[0])


def mapping(displayed):
    actual = {chr(i): '' for i in range(97, 104)}  # {us machine mei : ideal }
    setsdisplayed = list(map(set, displayed))
    cf = setsdisplayed[0]
    a = setsdisplayed[1].difference(cf)
    bd = setsdisplayed[2].difference(cf)
    for i in setsdisplayed[3:6]:
        if i.issuperset(cf):
            dg = i.difference(cf, a)
            break
    d = bd.intersection(dg)
    g = dg.difference(d)
    b = bd.difference(d)
    for i in setsdisplayed[3:6]:
        if i.issuperset(b):
            f = i.difference(a, b, d, g)
            break
    c = cf.difference(f)
    e = setsdisplayed[9].difference(a, b, c, d, f, g)
    actual[str(a)[2]] = 'a'
    actual[str(b)[2]] = 'b'
    actual[str(c)[2]] = 'c'
    actual[str(d)[2]] = 'd'
    actual[str(e)[2]] = 'e'
    actual[str(f)[2]] = 'f'
    actual[str(g)[2]] = 'g'
    return actual


cnt = 0

reality = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', "bcdf": '4',
           'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}


def fourdigit(disp):
    global reality
    mapp = mapping(disp[0])
    digs = [''.join(sorted(list(map(lambda x: mapp[x], j)))) for j in disp[1]]
    return int(''.join([reality[k] for k in digs]))


ans = 0
for i in sortedDisplay:
    ans += fourdigit(i)
print(ans)
