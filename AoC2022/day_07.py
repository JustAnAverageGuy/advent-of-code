from collections import defaultdict
from itertools import accumulate
from operator import concat

import aoc_helper

raw = aoc_helper.fetch(7, 2022)

"""
def parse_raw():
    # dictionary of dictionaries prob
    term = re.finditer(r'\$ ((?=cd)(?P<cd>cd) (?P<newdir>[^\n]*)|(?=ls)(?P<ls>ls).(?P<contents>[^\$]*)\n)',raw,re.DOTALL)
    
    folders = dict()
    pwd = []
    for i in term:
        if i.group("cd"):
            newd = i.group('newdir')
            assert newd
            if newd == '..':
                pwd.pop()
            elif newd == '/':
                pwd = ['/']
            else:
                pwd.append(newd)
                        
        else:
            assert i.group("ls") # deal with ls 
            cont = list(map(lambda x:tuple(x.split()) if x.split()[0] == 'dir' else (int(x.split()[0]),x.split()[1]),i.group("contents").split('\n')))
            print(cont)
            
            
            #exec('folders'+''.join(map(lambda x:f"[{x}]",pwd)))
    



data = parse_raw()
"""
"""

Solution copied from [u/bivaro6826]https://www.reddit.com/r/adventofcode/comments/zesk40/comment/izacel7/?utm_source=share&utm_medium=web2x&context=3

"""


total_space = 70000000
required_space = 30000000
max_size = 100000
curr_dir_path = list()
dir_tree = defaultdict(lambda: 0)


def keep_useful_info(entry):
    # keep only directory changes and file size
    return (True, entry[1]) if entry[0] == "$ cd" else (False, int(entry[0])) if entry[0][0].isdigit() else None


# with open('input.txt', 'r') as file:
commands = filter(bool, map(keep_useful_info, (line.strip(
    '\n').rsplit(' ', 1) for line in raw.splitlines())))
while True:
    try:
        change_dir, info = next(commands)
        if change_dir:
            curr_dir_path.pop() if info == ".." else curr_dir_path.append(info)
        else:
            # the name of a directory is its path
            for directory in accumulate(curr_dir_path, concat):
                dir_tree[directory] += info
    except StopIteration:
        break

# PART ONE
print(sum(filter(lambda x: x <= max_size, dir_tree.values())))

# PART TWO
# required space - free space
to_del_space = required_space - (total_space - dir_tree["/"])
print(to_del_space + min(filter(lambda x: x >= 0,
      map(lambda dir_size: dir_size - to_del_space, dir_tree.values()))))


def part_one():
    return sum(filter(lambda x: x <= max_size, dir_tree.values()))


def part_two():
    # required space - free space
    to_del_space = required_space - (total_space - dir_tree["/"])
    return to_del_space + min(filter(lambda x: x >= 0, map(lambda dir_size: dir_size - to_del_space, dir_tree.values())))


aoc_helper.lazy_submit(day=7, year=2022, solution=part_one)
aoc_helper.lazy_submit(day=7, year=2022, solution=part_two)
