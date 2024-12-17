from collections import Counter, defaultdict, deque
from itertools import count

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(17, 2024)


def parse_raw(raw: str):
    n = raw.splitlines()
    a = extract_ints(n[0])[0]
    b = extract_ints(n[1])[0]
    c = extract_ints(n[2])[0]
    pro = extract_ints(n[4])
    return ([a,b,c], pro)


data = parse_raw(raw)

def get_combo(registers, operand):
    assert 0<= operand <= 7
    if operand == 7: raise ValueError
    if operand <= 3: return operand
    return registers[operand & 0b11]


def interpret(initial_state):
    registers, memory = initial_state
    i_pr = 0
    out = []
    while 0 <= i_pr <= len(memory) - 1:

        opcode  = memory[i_pr]
        if i_pr+1 > len(memory) - 1: raise Exception("Segmentation Fault") 
        operand = memory[i_pr+1]

        i_pr += 2
        # now process the instruction

        if opcode == 0:
            b = get_combo(registers, operand)
            registers[0] >>= b
            continue

        if opcode == 1:
            registers[1] ^= operand
            continue

        if opcode == 2:
            registers[1] = get_combo(registers, operand) & 0b111
            continue

        if opcode == 3:
            if registers[0]: i_pr = operand
            continue
        
        if opcode == 4:
            registers[1] ^= registers[2]
            continue

        if opcode == 5:
            out.append(
                get_combo(registers, operand) & 0b111
            )
            continue

        if opcode == 6:
            b = get_combo(registers, operand)
            registers[1] = (registers[0] >> b)
            continue

        if opcode == 7:
            b = get_combo(registers, operand)
            registers[2] = (registers[0] >> b)
            continue

    return out
            


def part_one(data=data):
    out = ",".join(str(i) for i in interpret(data))
    return out


aoc_helper.lazy_test(day=17, year=2024, parse=parse_raw, solution=part_one)

def part_two(data=data):
     target = memory = data[1]
     prefixes = [0]
     tail = []
     for i in target[::-1]:
         nex = []
         tail.append(i)
         for prefix in prefixes:
             for d in range(8):
                 out = interpret(([ (prefix<<3) | d, 0, 0 ], memory))
                 if out[::-1] == tail:
                     nex.append( (prefix<<3) | d )
         prefixes = nex[::]
     return min(prefixes)


aoc_helper.lazy_test(day=17, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=17, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=17, year=2024, solution=part_two, data=data)
