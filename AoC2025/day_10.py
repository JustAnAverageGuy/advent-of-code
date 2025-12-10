import aoc_helper
from aoc_helper import ( extract_ints,)
import numpy as np
from scipy.optimize import linprog # had to update scipy version in the venv

raw = aoc_helper.fetch(10, 2025)


def parse_raw(raw: str):
    data = []
    for line in raw.splitlines():
        indicator, *buttons, joltages = line.strip().split()
        indicator_target = [i == '#' for i in indicator[1:-1]]
        buttons = [
            tuple(extract_ints(button)) for button in buttons
        ]
        joltages = tuple(extract_ints(joltages))
        data.append(
            (indicator_target, buttons, joltages)
        )
    return data


data = parse_raw(raw)

def min_button_press_count(target: list[bool], buttons: list[tuple[int,...]]) -> int:
    n = len(buttons)
    mi = n
    for mask in range(1 << n):
        if mask.bit_count() >= mi: continue
        ini = [False]*len(target)
        for j in range(n):
            if not (mask >> j)&1: continue
            for idx in buttons[j]:
                ini[idx] = not ini[idx]
        # print(f'{mask:{n}b}', ini, target)
        if ini != target: continue
        mi = mask.bit_count()
    # print(target, buttons, mi)
    return mi


def part_one(data=data):
    # print(max(len(button) for _,button,_ in data), len(data))
    ans = 0
    for target, buttons, _ in data:
        ans += min_button_press_count(target, buttons)
    return ans
        



aoc_helper.lazy_test(day=10, year=2025, parse=parse_raw, solution=part_one)

def min_increment_counts(target: list[int], buttons: list[tuple[int, ...]]) -> int:
    n = len(target)
    m = len(buttons)
    matrix = np.zeros((n,m), dtype=int)
    for j, button in enumerate(buttons):
        for i in button: 
            matrix[i,j] = 1
    # print(matrix)
    # print(m, np.linalg.matrix_rank(matrix))

    """hollow hollow victory, but yeah you gotta use the heavy machinery sometimes"""
    res = linprog(c=np.ones(m,dtype=int),A_eq=matrix, b_eq=target, integrality=True)
    assert res.success
    return round(res.fun)

def part_two(data=data):
    ans = 0
    for _, buttons, target in data:
        ans += min_increment_counts(target, buttons)
    return ans



aoc_helper.lazy_test(day=10, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2025, solution=part_two, data=data)
