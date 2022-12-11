import aoc_helper
import re
from aoc_helper import (
    iter,
    list,
    map,
    range,
)

raw = aoc_helper.fetch(11, 2022)

def parse_raw():
    pattern = re.compile(r'Monkey (?P<monkey>\d+):\n  Starting items:(?P<items>.*)\n  Operation: new = (?P<op>.*)\n  Test: divisible by (?P<testdivby>\d+)\n    If true: throw to monkey (?P<truethro>\d+)\n    If false: throw to monkey (?P<falsethro>\d+)')
    return list(map(lambda x:x.groupdict(),re.finditer(pattern,raw)))
    


data = parse_raw()
class monkey:
    """
    Class to store the attributes of a monkey
    """
    def __init__(self,mon_dict:dict[str,str]):
        self.name = int(mon_dict["monkey"])
        self.items = list(map(int,mon_dict["items"].split(',')))
        exec(f"self.op = lambda old: {mon_dict['op']}")
        self.div = int(mon_dict["testdivby"])
        self.tru = int(mon_dict["truethro"])
        self.fal = int(mon_dict["falsethro"])
    
    def __str__(self):
        return f'Monkey {self.name}: {",".join(map(str,self.items))}'    
    
    def catch(self,caught:list[int]):
        self.items.extend(caught)
        
    def monkey_around(self,worry:bool=True):
        """
        Simulate a monkey's turn
        """
        inspected = len(self.items)
        updated_worries = list(map(lambda x:x//3,list(map(self.op,self.items)))) if worry else list(map(lambda x: x%9699690,list(map(self.op,self.items)))) # HARD CODED UPDATED WORRIES AS IDK HOW TO, SINCE MOD VALUE DEPENDS ON THE GANG, ig I can use a big primorial as a modulo
        self.items = []
        return (self.tru,list(filter(lambda x: not (x%self.div),updated_worries))),(self.fal,list(filter(lambda x: (x%self.div),updated_worries))),inspected

class monkeygang:
    def __init__(self,monkeys:list[dict[str,str]]):
        self.gang = {int(i['monkey']):monkey(i) for i in monkeys}
        self.size = len(monkeys)
        self.inspected = {i:0 for i in self.gang.keys()}
    def round(self,worry:bool=True):
        for i in range(self.size):
            to_monkey_a,to_monkey_b,inspected = self.gang[i].monkey_around(worry)
            self.gang[to_monkey_a[0]].catch(to_monkey_a[1])
            self.gang[to_monkey_b[0]].catch(to_monkey_b[1])
            self.inspected[i] += inspected
    def round_n(self,n:int,worry:bool=True):
        for i in range(n):
            self.round(worry)
            if i % 100 == 0:
                print("=====Round "+str(i+1)+"=====")
                print(self.inspections())
    def __str__(self):
        return "\n".join(self.gang[j].__str__() for j in self.gang)
    def inspections(self):
        return '\n'.join(map(lambda x:f'Monkey {x} inspected items {self.inspected[x]} times.',sorted(self.gang.keys())))
    def part_one_answer(self):
        t=sorted(self.inspected.values())[-2:]
        return t[0]*t[1]

def part_one():
    m = monkeygang(data)
    m.round_n(20)
    print(m)
    print(m.inspections())
    print((t:=m.part_one_answer()))
    return t


def part_two():
    m = monkeygang(data)
    m.round_n(10000,False)
    print(m)
    print(m.inspections())
    print((t:=m.part_one_answer()))
    return t


#aoc_helper.lazy_submit(day=11, year=2022, solution=part_one)
#aoc_helper.lazy_submit(day=11, year=2022, solution=part_two)
