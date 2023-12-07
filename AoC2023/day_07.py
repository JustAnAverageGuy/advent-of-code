import aoc_helper
from aoc_helper import (
    map,
    range,
)

import sys
DAY = 7
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

bets = []

card_to_strength = dict(zip("AKQJT98765432J",range(13,-1,-1))) # language CHHEZE !

for i in raw.splitlines():
    hand, bet = i.split()
    bets.append(
        (
            tuple(map(lambda x: card_to_strength[x], hand.strip())),
            int(bet)
        )
    )
    

from collections import Counter

JOKER        = 0

FIVEOFAKIND  = 7
FOUROFAKIND  = 6
FULLHOUSE    = 5
THREEOFAKIND = 4
TWOPAIR      = 3
ONEPAIR      = 2
HIGHCARD     = 1

def strength(hand):
    c = Counter(hand).most_common()
    if len(c) == 1:                        return (FIVEOFAKIND, *hand)
    if len(c) == 2:
        if JOKER in hand:                  return (FIVEOFAKIND, *hand)
        if c[0][1] == 4:                   return (FOUROFAKIND, *hand)
        if c[0][1] == 3:                   return (FULLHOUSE,   *hand)
    if len(c) == 3:
        if c[0][1] == 3:
            if JOKER in hand:              return (FOUROFAKIND ,*hand)
            return                                (THREEOFAKIND,*hand)
        if c[0][1] == 2:
            if JOKER in [c[0][0],c[1][0]]: return (FOUROFAKIND, *hand)
            if c[2][0] == JOKER:           return (FULLHOUSE,   *hand)
            return                                (TWOPAIR,     *hand)
    if len(c) == 4: 
        if JOKER in hand:                  return (THREEOFAKIND,*hand)
        return                                    (ONEPAIR,     *hand)
    if JOKER in hand:                      return (ONEPAIR,     *hand)
    return                                        (HIGHCARD,    *hand)


s = 0
for i,j in enumerate(sorted(bets,key= lambda x: strength(x[0])),1): s += i*j[1]
print(s)