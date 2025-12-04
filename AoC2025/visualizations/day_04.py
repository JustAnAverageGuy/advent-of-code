import aoc_helper
from aoc_helper import Grid
from colorist import *
import time
import sys

DELAY = "DELAY" in sys.argv
EXAMPLE = "EXAMPLE" in sys.argv

import math
from typing import Callable


try:

    print()
    print('\x1b[?25l',end='') # hide cursor
    def pprint(*args, **kwargs): 
        delay      = kwargs.get("delay", DELAY) 
        delay_time = kwargs.get("delay_time", 0.1)
        if "delay" in kwargs: del kwargs["delay"]
        if "delay_time" in kwargs: del kwargs["delay_time"]
        print(*args, **kwargs, flush=True)
        if delay: time.sleep(delay_time)
        

    raw = aoc_helper.fetch(4,2025) if not EXAMPLE else aoc_helper.get_sample_input(day=4,part=1,year=2025)[0] 

    data = Grid.from_string(raw,classify=lambda x: {'@':1, '.':0}[x])

    total_removed = 0
    while True:
        pprint("\033[3H",end="")
        accessible = 0
        to_be_removed = []
        for y in range(data.height):
            for x in range(data.width):
                if not data.get(x,y): 
                    pprint('⬛',end='')
                    continue
                if not sum(v for _, v in data.neighbours(x,y)) <4: 
                    pprint('⬜',end='')
                    continue
                # for (nx,ny),_ in data.neighbours(x,y):
                pprint('🟥',end='')
                to_be_removed.append((x,y))
            pprint()
        if not to_be_removed: break
        total_removed += len(to_be_removed)
        for x,y in to_be_removed: data[x,y] = 0


    pprint('_'*140)
    pprint(
    f"""
    {' '*20}[{Effect.DIM}Part{Effect.DIM_OFF} {BrightColor.CYAN}II{BrightColor.OFF}] {Effect.DIM}Total Squares Removed:{Effect.DIM_OFF} {total_removed}
    """
    )
    print('\x1b[?25h',end='') # show cursor
except KeyboardInterrupt:
    print(BrightColor.OFF,Color.OFF,'\x1b[?25h')
    bright_red("******\n*DEAD*\n******")
finally:
    print(BrightColor.OFF,Color.OFF,'\x1b[?25h')

