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
    range,
    tail_call,
)
import sys
from colorist import *

DAY = 13
YEAR = 2023

EXAMPLE = "EXAMPLE" in sys.argv
TWO = "2" in sys.argv

if EXAMPLE:
    if TWO:
        raw, answer = aoc_helper.get_sample_input(day=DAY, year=YEAR, part=2)
    else: 
        raw, answer = aoc_helper.get_sample_input(day=DAY, year=YEAR, part=1)
else:
    raw = aoc_helper.fetch(DAY, YEAR)

sand_dunes = raw.split('\n\n')

def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{BrightColor.CYAN}[INFO]{BrightColor.OFF} {BrightColor.GREEN}{func.__name__}{BrightColor.OFF}{Effect.DIM}{args}{Effect.OFF}{(", kwargs="+str(kwargs)) if kwargs else ""} = {res}')
        # print(f'{BrightColor.CYAN}[INFO]{BrightColor.OFF} result= {res}')
        return res
    return wrapper
@log
def convert_to_row_col(dune:str):
    dune = dune.splitlines()
    h = len(dune)
    w = len(dune[0])
    rows = []
    cols = []
    for i in dune: rows.append(int("".join(map(lambda x: {'#':'1','.':'0'}[x],i)),2))
    for j in range(w): cols.append(int("".join(map(lambda x: {'#':'1','.':'0'}[x],(dune[i][j] for i in range(h)))),2))
    return rows, cols

def ispow2(n): return (n&(n-1) == 0) and n

@log
def check(a,b):
    A = [x^y for x,y in zip(a,b)]
    A.sort()
    # return A[-1] == 0 # part 1
    return ispow2(A[-2]) and (len(A) <= 2 or A[-3] == 0) # part 2

def find_mirror(hashes:list[int]):
    a = hashes[:: 1]
    b = hashes[::-1]
    n = len(a)
    for i in range(1,n,2):
        if check(a[:i+1], b[n-i-1:]): return (i+1) // 2
        if check(a[n-i-1:], b[:i+1]): return n - (i+1)//2
    return 0
s = 0

for dune in sand_dunes:
    r,c = convert_to_row_col(dune)
    x = 100*find_mirror(r) + find_mirror(c)
    s+=x
    # print(f'dune : {x}')
bright_yellow(s)