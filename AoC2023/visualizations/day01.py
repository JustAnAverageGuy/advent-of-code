import time
import aoc_helper
import colorist as cl

import sys

raw = aoc_helper.fetch(1, 2023)

delay = 'DELAY' in sys.argv

def parse_raw(raw):
    return raw.splitlines()


data = parse_raw(raw)


def part_one(data):
    s = 0
    c = 1
    for i in data:
        max_digs = 0
        for j in i:
            if j in "1234567890":  max_digs += 1
        digs = []
        print(f'{c:3}: ',end='')
        for j in i:
            if j in "1234567890": 
                digs.append(j)
                
                print(f'{cl.BrightColor.GREEN if len(digs) in [1,max_digs] else cl.Color.YELLOW}{j}{cl.BrightColor.OFF}',end='',flush=True)
                if delay:time.sleep(0.1)
            else:
                print(f'{cl.Effect.DIM}{j}{cl.Effect.DIM_OFF}',end='',flush=True)
                if delay:time.sleep(0.01)
                
        print()
        c += 1
        s += int(digs[0]+digs[-1])
    return s




try:
    cl.bright_cyan('\n'+"*"*10 +'\n' + str(part_one(data) ))
except KeyboardInterrupt:
    print(cl.BrightColor.OFF,cl.Color.OFF)
    cl.bright_red("******\n*DEAD*\n******")
