from collections import Counter, deque
import aoc_helper

raw = aoc_helper.fetch(22, 2024)


def parse_raw(raw: str):
    return [int(i) for i in raw.splitlines()]


data = parse_raw(raw)


class PRNG:
    def __init__(self, seed:int):
        self.seed = seed
        self.mask = (1 << 24) - 1
    def nex(self):
        self.seed ^= ((self.seed << 6) & self.mask)
        self.seed ^= ((self.seed >> 5) & self.mask)
        self.seed ^= ((self.seed << 11) & self.mask)
        return self.seed

def part_one(data=data):
    sm = 0
    for d in data:
        c = PRNG(d)
        for i in range(2000):
            s = c.nex()
        sm += s
    return sm



aoc_helper.lazy_test(day=22, year=2024, parse=parse_raw, solution=part_one)

def part_two(data=data):
    counter = Counter()
    for d in data:
        cur = set()
        c = PRNG(d)
        a = deque(maxlen=4)
        last = d%10
        for i in range(2000): 
            nx = c.nex() % 10
            a.append((nx - last))
            t = tuple(a)
            if t not in cur and (len(t) == 4): 
                counter[t] += nx
                cur.add(t)
            last = nx
    return counter.most_common(1)[0][1]

aoc_helper.lazy_test(day=22, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=22, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=22, year=2024, solution=part_two, data=data)
