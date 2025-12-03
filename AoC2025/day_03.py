import aoc_helper

raw = aoc_helper.fetch(3, 2025)


def parse_raw(raw: str):
    return [line.strip() for line in raw.splitlines()]


data = parse_raw(raw)

def get_max_pair(line):
    max_left = [line[0]]
    for i in line[1:]:
        max_left.append(
            max(max_left[-1], i)
        )
    
    return max( int(f'{max_left[i-1]}{line[i]}') for i in range(len(line) -1 , 0, -1))


def part_one(data=data):
    return sum(map(get_max_pair, data))



aoc_helper.lazy_test(day=3, year=2025, parse=parse_raw, solution=part_one)

def get_max_12(line):
    # dp[i][k] = max(dp[i-1][k-1] + s[i], dp[i-1][k])
    dp = [0]*13
    for i,c in enumerate(line):
        for k in range(12, -1,-1):
            if k > i + 1: dp[k] = float('-inf'); continue
            if k == 0: dp[k] = 0; continue
            dp[k] = max(dp[k-1]*10 + int(c), dp[k])
    return dp[12]





def part_two(data=data):
    return sum(map(get_max_12, data))


aoc_helper.lazy_test(day=3, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2025, solution=part_two, data=data)
