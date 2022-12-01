with open("AoC2020_Day1_input.txt", 'r') as file:
    p = list(map(int, file.readlines()))


def findSuM(n, listofnums):
    for i in listofnums:
        if n-i in listofnums:
            return (i, n-i)
    return "Nope"


for i in p:
    q = findSuM(2020-i, p)
    if q[0] != "N":
        print(i * q[0] * q[1])
        break
