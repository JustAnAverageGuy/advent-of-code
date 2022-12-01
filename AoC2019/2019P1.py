with open(r"AoC2019\AoC2019_Day1_input.txt", 'r') as f:
    m = map(lambda x: int(x.strip()), f.readlines())

# part 1
#print(sum(map(lambda x: x//3 - 2, m)))

# part 2


def totfuel(m):
    req = m//3 - 2
    extra = req//3 - 2 if req//3 - 2 > 0 else 0
    while extra > 0:
        req += extra
        extra = extra//3 - 2
    return req


print(totfuel(100756))
print(sum(map(lambda x: totfuel(x), m)))
