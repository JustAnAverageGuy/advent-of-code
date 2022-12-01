with open("AoC2020_Day2_input.txt", 'r') as file:
    crrpt = file.readlines()


def isAllowedOld(policy):
    a, b = policy.index(r'-'), policy.index(r':')
    atleast, atmost = int(policy[:a]), int(policy[a+1:b-1])
    requi = policy[b-1]
    # -1 due to the fact that policy also has requi at the index b-1 and hence count in the password is one more than the actual count
    return atleast <= policy.count(requi) - 1 <= atmost


def isAllowedNew(policy):
    a, b = policy.index(r'-'), policy.index(r':')
    index1, index2 = int(policy[:a]), int(policy[a+1:b-1])
    requi = policy[b-1]
    return (policy[index1 + b+2 - 1] == requi) ^ (policy[index2 + b+2 - 1] == requi)


cnt = 0
for i in crrpt:
    if isAllowedNew(i):
        cnt += 1
print(cnt)

with open('output.txt', 'w') as file:
    for i in crrpt:
        file.write(f"{i.strip() : <40}{isAllowedNew(i)} \n")
