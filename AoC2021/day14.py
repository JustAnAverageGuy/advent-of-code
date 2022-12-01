from collections import Counter


rules = {chr(i)+chr(j): '' for i in range(ord('A'), ord('Z')+1)
         for j in range(ord('A'), ord('Z')+1)}

with open("input14.txt", 'r') as file:
    template = file.readline().strip()
    file.readline()
    for i in map(lambda x: x.strip().split(' -> '), file.readlines()):
        rules[i[0]] = i[1]


def nex(poly, rule=rules):
    ans = ''
    for i in range(len(poly)-1):
        ans += poly[i]+rule[poly[i:i+2]]
    ans += poly[-1]
    return ans


def growpolymer(n, temp=template, rule=rules):
    ans = temp
    for _ in range(n):
        ans = nex(ans, rule)
    return ans


hmm = growpolymer(10)
b = Counter(hmm)
print(max(b.values()) - min(b.values()))
