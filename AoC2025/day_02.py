import aoc_helper
from bisect import bisect_left, bisect_right


raw = aoc_helper.fetch(2, 2025)


def parse_raw(raw: str):
    ans = []
    for i in raw.split(","):
        x = i.split("-")
        ans.append((int(k) for k in x))
    return ans


data = parse_raw(raw)

invalid_numbers_1 = [int(str(i) * 2) for i in range(1_000_000)]


def sum_in_range(nums, start, end):
    r = bisect_left(nums, end)
    l = bisect_right(nums, start) + 1
    return sum(nums[l : r + 1])


def part_one(data=data):
    ans = 0
    for a, b in data:
        ans += sum_in_range(invalid_numbers_1, a, b)
    return ans


aoc_helper.lazy_test(day=2, year=2025, parse=parse_raw, solution=part_one)

nums = {
    int(str(i) * k)
    for i in range(1, 1_000_000)
    for k in range(2, 8)
    if len(str(i) * k) <= 11
}
for i in range(1, 10):
    nums.add(int(f"{i}" * 11))


invalid_numbers_2 = sorted(nums)


def part_two(data=data):
    ans = 0
    for a, b in data:
        ans += sum_in_range(invalid_numbers_2, a, b)
    return ans


aoc_helper.lazy_test(day=2, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2025, solution=part_two, data=data)
