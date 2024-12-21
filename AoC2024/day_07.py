import aoc_helper

raw = aoc_helper.fetch(7, 2024)


def parse_raw(raw: str):
    a = []
    for i in raw.splitlines():
        x,y = i.split(':',maxsplit=1) 
        a.append((int(x), [int(k) for k in y.split()]))
    return a


data = parse_raw(raw)

def evalu(a, operations):
    b = a[::-1]
    for i in operations:
        x,y = b.pop(), b.pop()
        if i == 1: b.append(x*y)
        else: b.append(x+y)
    # print(a, operations, b)
    return b[0]

def evalu2(a, operations):
    b = a[::-1]
    for i in operations:
        x,y = b.pop(), b.pop()
        if i == 1: b.append(x*y)
        elif i == 2: b.append(x+y)
        else: b.append(int(f'{x}{y}'))
    # print(a, operations, b)
    return b[0]

def part_one(data=data):
    ans = 0
    for target, hmm in data:
        n = len(hmm)
        for mask in range(1<<(n-1)):
            ops = []
            temp = mask
            for j in range(n-1):
                ops.append(temp & 1)
                temp >>= 1
            ev = evalu(hmm, ops)
            if ev == target: 
                ans += target
                break
    return ans


aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_one)

def part_two(data=data):
    ans = 0
    for target, hmm in data:
        n = len(hmm)
        for mask in range(3**(n-1)):
            ops = []
            temp = mask
            for j in range(n-1):
                ops.append(temp % 3)
                temp //= 3
            ev = evalu2(hmm, ops)
            if ev == target: 
                ans += target
                break
    return ans   


aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2024, solution=part_two, data=data)
