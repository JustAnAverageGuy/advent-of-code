import aoc_helper
from colorist import *
import time
import sys
from math import log2
DELAY = "DELAY" in sys.argv

print()
print('\x1b[?25l',end='')
def pprint(*args, **kwargs): 
    delay      = kwargs.get("delay", DELAY) 
    delay_time = kwargs.get("delay_time", 0.1)
    if "delay" in kwargs: del kwargs["delay"]
    if "delay_time" in kwargs: del kwargs["delay_time"]
    print(*args, **kwargs, flush=True)
    if delay: time.sleep(delay_time)
    

data = aoc_helper.fetch(4,2023)

N = len(data)
tot_counts = {i: 1 for i in range(N)}
tot_score = 0
for idx,i in enumerate(data.splitlines()):
    sid, card_data = i.split(":")
    swin, smine = card_data.split("|")
    win  = aoc_helper.extract_ints(swin)
    mine = aoc_helper.extract_ints(smine)
    intersect = set(win) & set(mine)
    
    for hmm in range(2):
        if not hmm:
            pprint(sid,end=': ')
            for j in win: pprint(f'{Effect.DIM}{j:2}{Effect.DIM_OFF}',end=' ')
            pprint('|',end=' ')
            for j in mine:
                pprint(f'{Effect.DIM}{j:2}{Effect.DIM_OFF}',end=' ')
            pprint('|',end='\r')
        else:
            pprint(sid,end=': ', delay_time=0.01)
            for j in win:
                if j in intersect: pprint(f'{BrightColor.YELLOW}{j:2}{BrightColor.OFF}',end=' ', delay_time=0.01)
                else: pprint(f'{Effect.DIM}{j:2}{Effect.DIM_OFF}',end=' ', delay_time=0.01)
            pprint('|',end=' ', delay_time=0.01)
            for j in mine:
                if j in intersect: pprint(f'{BrightColor.YELLOW}{j:2}{BrightColor.OFF}',end=' ', delay_time=0.01)
                else: pprint(f'{Effect.DIM}{j:2}{Effect.DIM_OFF}',end=' ', delay_time=0.01)
            
            common = len(intersect)
            score = (1 << (common - 1)) if common else 0
            if common:
                for k in range(idx+1,idx+common+1):
                    if k >= N: break
                    tot_counts[k] += tot_counts[idx]
            tot_score += score
            if common: 
                pprint(f'| {Color.GREEN}{common:2}{Color.OFF} -> {Effect.DIM}{score:3}{Effect.DIM_OFF} [{Effect.DIM}{tot_counts[idx]:^8}{Effect.DIM_OFF}] {BrightColor.MAGENTA}{("#"*int(log2(tot_counts[idx]))):<30}{BrightColor.OFF}', delay=False)
            else:
                pprint(f'|           [{Effect.DIM}{tot_counts[idx]:^8}{Effect.DIM_OFF}] {Effect.DIM}{Color.MAGENTA}{("#"*int(log2(tot_counts[idx]))):<30}{Color.OFF}{Effect.DIM_OFF}', delay=False)

pprint('_'*140)
pprint(
f"""
{' '*20}[{Effect.DIM}Part{Effect.DIM_OFF} {BrightColor.CYAN}I {BrightColor.OFF}] {Effect.DIM}Total Score:{Effect.DIM_OFF} {tot_score}
{' '*20}[{Effect.DIM}Part{Effect.DIM_OFF} {BrightColor.CYAN}II{BrightColor.OFF}] {Effect.DIM}Total Cards:{Effect.DIM_OFF} {sum(tot_counts.values())}
"""
)
print('\x1b[?25h',end='')
