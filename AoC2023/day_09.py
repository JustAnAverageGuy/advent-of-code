import aoc_helper
from aoc_helper import (extract_ints,range,)
from colorist import *

import sys

DAY = 9
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

histories = []

for line in raw.splitlines():
    histories.append(extract_ints(line))

def extrapolate(hist):
    n = len(hist)
    if TWO: hist = hist[::-1]
    hmm = [hist,]
    for i in range(n-1): hmm.append([0]*(n-i-1))
    for i in range(n-1):
        for k, a in enumerate(zip(hmm[i], hmm[i][1:])):
            hmm[i+1][k] = a[1] - a[0]
    for i in range(n-1, 0, -1):
        hmm[i-1].append(
            hmm[i][-1] + hmm[i-1][-1]
        )
    return (hmm[0][-1])


s= 0

# import numpy as np

# for hist in histories:
#     data = np.array(hist)
#     n = len(data)
    
#     fit = np.polyfit(list(range(0,n)), hist, n-1)
#     line = np.poly1d(fit)

#     s += int(line(n))

# print(s)
for i in histories: s += extrapolate(i)
bright_green(s)