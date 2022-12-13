from ast import literal_eval
from functools import cmp_to_key
import aoc_helper

raw = aoc_helper.fetch(13, 2022)


def parse_raw_one():
    return [(i, literal_eval(t.replace('\n', ','))) for i, t in enumerate(raw.split('\n\n'), 1)]


data_1 = parse_raw_one()


def parse_raw_two():
    return [literal_eval(i) for i in raw.split()] + [[[2]], [[6]]]


data_2 = parse_raw_two()


def compare(l1, l2):
    if type(l1) == int and type(l2) == int:
        return 'hmm' if (l1 == l2) else l1 < l2
    if type(l1) == list and type(l2) == list:
        k = 0
        while True:
            if k < len(l1) and k < len(l2):
                if compare(l1[k], l2[k]) == 'hmm':
                    k += 1
                else:
                    return compare(l1[k], l2[k])
            else:
                return 'hmm' if (len(l1) == len(l2)) else (len(l1) < len(l2))
    assert ((type(l1), type(l2)) in {(int, list), (list, int)})
    if type(l1) == list:
        return compare(l1, [l2])
    if type(l2) == list:
        return compare([l1], l2)


assert (compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))
assert (compare([[1], [2, 3, 4]], [[1], 4]))
assert (not compare([9], [[8, 7, 6]]))


def part_one():
    return sum(i[0] for i in data_1 if compare(i[1][0], i[1][1]))


def part_two():
    k = sorted(data_2, key=cmp_to_key(lambda x, y: 1 - 2 * compare(x, y)))
    return (k.index([[2]]) + 1)*(k.index([[6]]) + 1)


aoc_helper.lazy_submit(day=13, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=13, year=2022, solution=part_two)
