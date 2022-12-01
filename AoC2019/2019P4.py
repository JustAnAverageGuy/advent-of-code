with open(r"AoC2019\AoC2019_Day4_input.txt", 'r') as f:
    a, b = map(int, f.read().split('-'))


def group(t):
    t += 'a'
    A = []
    k = 1
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            k += 1
        else:
            A.append((t[i], k))
            k = 1
    return A


def check(n):
    t = str(n)
    if int(''.join(sorted([i for i in t]))) != n or (len(set(t)) == len(t)) or not any((i[1] == 2 for i in group(t))):
        return False
    return True


print(len(list(filter(check, range(a, b+1)))))
