import aoc_helper
from colorist import *
import time
import sys

DELAY = "DELAY" in sys.argv
EXAMPLE = "EXAMPLE" in sys.argv

import math
from typing import Callable

def delay_between_loops(index: int,
                        total: int,
                        duration: float,
                        easing: Callable[[float], float],
                        min_delay: float = 0.0,
                        max_delay: float | None = None) -> float:
    if total <= 1:
        return max(min_delay, duration)
    t = index / (total - 1)
    eased = easing(t)
    if index < total - 1:
        eased_next = easing((index + 1) / (total - 1))
        slice_fraction = eased_next - eased
    else:
        eased_prev = easing((index - 1) / (total - 1))
        slice_fraction = eased - eased_prev
    delay = slice_fraction * duration
    if min_delay:
        delay = max(delay, min_delay)
    if max_delay is not None:
        delay = min(delay, max_delay)
    return delay

def ease_in_out_circ(x: float) -> float:
    if x < 0.5:
        return (1 - math.sqrt(1 - (2 * x) ** 2)) / 2
    return (math.sqrt(1 - (-2 * x + 2) ** 2) + 1) / 2

def ease_in_out_expo(x: float) -> float:
    if x == 0:
        return 0.0
    if x == 1:
        return 1.0
    if x < 0.5:
        return math.pow(2, 20 * x - 10) / 2
    return (2 - math.pow(2, -20 * x + 10)) / 2


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
        

    data = aoc_helper.fetch(3,2025) if not EXAMPLE else aoc_helper.get_sample_input(day=3,part=1,year=2025)[0] 

    K = 12

    N = len(data.splitlines())
    tot_score = 0
    for idx,line in enumerate(data.splitlines()[60:80]):
        pprint(f'Bank {idx+1:3}:', end=' ', delay=0.005)
        dp = [(0, [])]*(K+1)
        # delay_time = delay_between_loops(
        #     index=idx,
        #     total=N,
        #     duration=30/200,
        #     easing=ease_in_out_expo,
        # )
        delay_time =  0.01
        for i,c in enumerate(line):
            pprint(f'{""}{c}{""}',end="", delay_time=delay_time)
            for taken_count in range(K, 0,-1):
                if taken_count > i + 1: dp[taken_count] = (float('-inf'), []); continue
                if dp[taken_count][0] < dp[taken_count-1][0]*10 + int(c):
                    # le rhe is element ko
                    dp[taken_count] = (dp[taken_count-1][0]*10 + int(c), [*dp[taken_count-1][1], i])
                    ...
                else:
                    # nhi le rhe c in answer
                    ... 
        pprint('\r',end='')
        pprint(f'Bank {idx+1:3}:', end=' ', delay=0.001)

        indices = dp[K][1]
        for i, c in enumerate(line):
            if i in indices:
                pprint(f'{BrightColor.YELLOW}{c}{BrightColor.OFF}',end='',delay_time=delay_time)
            else:
                pprint(f'{Effect.DIM}{c}{Effect.DIM_OFF}',end='',delay_time=delay_time)

        pprint(f' -> {BrightColor.GREEN}{dp[K][0]}{BrightColor.OFF}')

        tot_score += dp[K][0]
    pprint('_'*140)
    pprint(
    f"""
    {' '*20}[{Effect.DIM}Part{Effect.DIM_OFF} {BrightColor.CYAN}II{BrightColor.OFF}] {Effect.DIM}Total joltage:{Effect.DIM_OFF} {tot_score}
    """

    # """
    # {' '*20}[{Effect.DIM}Part{Effect.DIM_OFF} {BrightColor.CYAN}II{BrightColor.OFF}] {Effect.DIM}Total Cards:{Effect.DIM_OFF} {sum(tot_counts.values())}
    # """
    )
    print('\x1b[?25h',end='') # show cursor
except KeyboardInterrupt:
    print(BrightColor.OFF,Color.OFF,'\x1b[?25h')
    bright_red("******\n*DEAD*\n******")
finally:
    print(BrightColor.OFF,Color.OFF,'\x1b[?25h')

