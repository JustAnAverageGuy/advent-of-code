# coding: utf-8
import aoc_helper

raw = aoc_helper.fetch(19, 2024)

def parse_raw(raw: str):
    a, b = raw.split("\n\n")
    patterns = a.split(', ')
    designs = b.splitlines()
    return patterns, designs

data = parse_raw(raw)

# def is_possible(x:str, patterns):
#     if x == "": return True
#     for i in patterns:
#         if x.startswith(i):
#             a = is_possible(x[len(i):],patterns)
#             if a: return True
#     return False

patterns = data[0]

# basis = []
# for i in range(len(patterns)):
#     modif = [*patterns[:i], *patterns[i+1:]]
#     if not is_possible(patterns[i], modif): basis.append(patterns[i])

from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
r = f'({"|".join(patterns)})+'
s = NFA.from_regex(r)
d = DFA.from_nfa(s)

part_1 = 0
for i in data[1]:
    if i in d: part_1 += 1
print(part_1)
