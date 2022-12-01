with open("input3.txt", 'r') as file:
    report = [i.strip() for i in file.readlines()]


def rate(data):
    gans = ''
    eans = ''
    i = len(data[0])
    cnt = [0]*i
    for n in data:
        for j in range(i):
            if n[j] == '1':
                cnt[j] += 1
            else:
                cnt[j] -= 1
    for k in cnt:
        if k > 0:
            gans += '1'
            eans += '0'
        else:
            gans += '0'
            eans += '1'
    return gans, eans

# gans, eans = gamma, epsilon etc.


def mostcommonbit(data, i):
    cnt = 0
    for k in data:
        if k[i] == '0':
            cnt -= 1
        else:
            cnt += 1
    return '0' if (cnt < 0) else '1'


def leastcommonbit(data, i):
    cnt = 0
    for k in data:
        if k[i] == '0':
            cnt -= 1
        else:
            cnt += 1
    return '1' if (cnt < 0) else '0'


""" 
gans = ''
eans = ''
for i in range(len(report[0])):
    gans += mostcommonbit(report, i)
    eans += leastcommonbit(report, i)
print(gans, eans)
print(rate(report)) """
# print(rate(report))

# Part 2


def health(data):
    p, q = data, data
    i, j = 0, 0
    while len(p) > 1:
        p = list(filter(lambda x: (x[i] == mostcommonbit(p, i)), p))
        i += 1
    while len(q) > 1:
        q = list(filter(lambda x: (x[j] == leastcommonbit(q, j)), q))
        j += 1
    return int(p[0], 2), int(q[0], 2)


t = health(report)

print(t[0]*t[1])
