with open("AoC2020_Day6_input.txt", 'r') as file:
    huh = [i.split() for i in file.read().split('\n\n')]


# PART 1
""" cnt = 0
for i in huh:
    cnt += len({k for j in i for k in j})
print(cnt)
 """


# PART 2
cnt = 0
for i in huh:
    p = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    t = len(i)
    for k in i:
        for s in k:
            p[s] += 1
    for k in p:
        if p[k] == t:
            cnt += 1

print(cnt)
