with open("input6.txt", 'r') as file:
    fish = list(map(int, file.readline().split(',')))


""" def nexnday(fish, n):
    a = list(map(lambda x: x-n, fish))
    for i in range(len(a)):
        if a[i] == -1:
            a[i] = 6
            a.append(8)
    return a, len(a)


fish = [3, 4, 3, 1, 2]


i = 0
while i < 150:
    p = min(fish) + 1
    fish, schoolsize = nexnday(fish, p)
    i += p

print(schoolsize)
 """


# fish = [3, 4, 3, 1, 2]

fishcnt = {i: fish.count(i) for i in range(9)}
# print(fishcnt)


def nextday(fishdata):
    updatedfishdata = {i: fishdata[i+1] for i in range(8)}
    updatedfishdata[6] += fishdata[0]
    updatedfishdata[8] = fishdata[0]
    return updatedfishdata


def populationonnthday(n, fishcnt):
    for _ in range(n):
        fishcnt = nextday(fishcnt)
    return sum(fishcnt.values())


with open("output.txt", 'w') as file:
    for i in range(50):
        file.write(f"(\\ln({populationonnthday(i,fishcnt)})),")
