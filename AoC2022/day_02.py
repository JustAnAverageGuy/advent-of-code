import aoc_helper


raw = aoc_helper.fetch(2, 2022)


def parse_raw():
    return [i.split() for i in raw.splitlines()]


data = parse_raw()  # [("A","Y"),..]


def part_one():
    rps = {"A": 'r', "X": 'r', "B": 'p', "Y": 'p',
           "C": 's', "Z": 's'}  # translate abcxyz to rps
    rpscore = {'r': 1, "p": 2, "s": 3}  # values of rps
    loss = 'rspr'
    score = 0
    for i in data:
        score += rpscore[rps[i[1]]]
        if rps[i[0]] == rps[i[1]]:
            score += 3
        elif (rps[i[0]]+rps[i[1]]) in loss:
            score += 0
        else:
            score += 6
    return score


def part_two():
    hardcode = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, ('B', 'X'): 1,
                ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7} # calculated by human
    score = 0
    for i in data:
        score += hardcode[i]
    return score

# part_one: 13009, part_two: 10398
aoc_helper.lazy_submit(day=2, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=2, year=2022, solution=part_two)
