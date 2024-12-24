from operator import and_, or_, xor

import aoc_helper

raw = aoc_helper.fetch(24, 2024)


def parse_raw(raw: str):
    initials, connections = raw.split("\n\n")
    ini = dict()
    connec = dict()
    for i in initials.splitlines():
        x, y = i.split(':')
        assert x not in ini
        ini[x] = int(y.strip())
    for j in connections.splitlines():
        l, op, r, _, res = j.strip().split()
        assert res not in connec
        connec[res] = (l, r, op)
    return (ini, connec)


data = parse_raw(raw)

def part_one(data=data):
    ini, conn = data
    nodes = set()
    dependencies = dict()
    for k, (i,j,_) in conn.items():
        nodes.add(i)
        nodes.add(j)
        nodes.add(k)
    for x in ini: nodes.add(x)
    for n in nodes:
        depe = set()
        stk = [n]
        while stk:
            x = stk.pop()
            if x in depe: continue
            if x in conn:
                l, r, _ = conn[x]
                depe.add(l)
                depe.add(r)
                stk.append(l)
                stk.append(r)
        dependencies[n] = depe

    for n, r in dependencies.items():
        if n in r: 
            # print(f"{c} Loop: {n} {r}")
            assert False

    final_vals = {i:None for i in nodes}
    
    def calc(x):
        if final_vals[x]is not None: return final_vals[x]
        if x not in conn:
            assert x in ini
            final_vals[x] = ini[x]
            return final_vals[x]
        l,r,op = conn[x]
        ll = calc(l)
        rr = calc(r)
        opp = {
            "AND":and_,
            "OR":or_,
            "XOR":xor,
        }[op]
        final_vals[x] = opp(ll, rr)
        return final_vals[x]

    z = 0
    for n in nodes:
        if n.startswith('z'):
            x = calc(n)
            z |= (x<<(int(n[1:])))
    return z

aoc_helper.lazy_test(day=24, year=2024, parse=parse_raw, solution=part_one)

### MAYBE THERE IS A SOLUTION USING THIS LOGIC, I AM TOO TIRED TO CHECK
# import re
# connection = data[1]
# def check_substitute(i):
#     l, r, op = connection[i]
#     to_rename = []
#     l,r = sorted([l,r])
#
#     if re.match(r'^x\d+$', l) and re.match(r'^y\d+',r):
#         n = r[1:]
#         if op == "AND":
#             if n == "00":  to_rename.append((i, f'c{n}'))
#             else: to_rename.append( (i, f'a{n}')  )
#         elif op  == "XOR":
#             if n == "00":  to_rename.append((i, f'z{n}'))
#             else: to_rename.append( (i, f'r{n}')  )
#
#     elif re.match(r'^c\d+$', l) and re.match(r'^r\d+',r):
#         n = r[1:]
#         if op == "AND":
#             to_rename.append((i, f't{n}'))
#         elif op == "XOR":
#             to_rename.append((i, f'z{n}'))
#     elif re.match(r'^a\d+$', l) and re.match(r'^t\d+',r):
#         n = r[1:]
#         if op in ["OR", "XOR"]:
#             to_rename.append((i, f'c{n}'))
#     return to_rename
#
# def clean(n):
#     for i in connection

import networkx as nx

ini, conn = data
graph = nx.DiGraph()

import re

invalid = [
    "z24", "fpq",
    "z07", "nqk", # possibly
    "fgt", "pcp",
    "srn", "z32"
]

aoc_helper.submit(
    24,2,
    ",".join(sorted(invalid))
)

swaps = {
    "z07":"nqk",
    "fgt":"pcp",
    "z24":"fpq",
    "srn":"z32"
}
two_way_swaps = dict() 
for i,j in swaps.items():
    two_way_swaps[i] = j
    two_way_swaps[j] = i
swaps = two_way_swaps
mod_conn = dict()
for i, j in conn.items():
    iprime = swaps.get(i, i)
    mod_conn[iprime] = j 

for i, (l,r,op) in mod_conn.items():
    dummy = f'{op}{l}{r}'
    graph.add_node(dummy, label=op)
    l, r = sorted([l,r])
    if re.match(r'^x\d+$', l) and re.match(r'^y\d+$',r):
        n = r[1:]
        graph.add_node(l,color="blue" )
        graph.add_node(r,color="red" )
        if op == "AND":
            if n == "00":  
                graph.add_node(i, label=f'c{n}', tooltip=i)
            else: 
                graph.add_node( i, label=f'a{n}', tooltip=i)
        elif op  == "XOR":
            if n == "00":
                graph.add_node(i, label=f'z{n}', color="green", tooltip=i)
            else:
                graph.add_node(i, label=f'r{n}', tooltip=i)
    if re.match(r'^z\d+$', i):
        graph.add_node(i, color="green")
    graph.add_edge(l, dummy)
    graph.add_edge(r, dummy)
    graph.add_edge(dummy, i)

from networkx.drawing.nx_pydot import write_dot

write_dot(graph, "day_24.gv")

def check_addition(xi, yi, swaps):
    ini, conn = data
    xi.extend([0]*(46 - len(xi)))
    yi.extend([0]*(46 - len(yi)))
    two_way_swaps = dict() 
    for i,j in swaps.items():
        two_way_swaps[i] = j
        two_way_swaps[j] = i

    swaps = two_way_swaps
    for i in range(len(xi)): ini[f'x{i:02}'] = xi[i]
    for i in range(len(yi)): ini[f'y{i:02}'] = yi[i]
    mod_conn = dict()
    for i, j in conn.items():
        iprime = swaps.get(i, i)
        mod_conn[iprime] = j 
    

    nodes = set()
    dependencies = dict()
    for k, (i,j,_) in mod_conn.items():
        nodes.add(i)
        nodes.add(j)
        nodes.add(k)
    for x in ini: nodes.add(x)
    for n in nodes:
        depe = set()
        stk = [n]
        while stk:
            x = stk.pop()
            if x in depe: continue
            if x in mod_conn:
                l, r, _ = mod_conn[x]
                depe.add(l)
                depe.add(r)
                stk.append(l)
                stk.append(r)
        dependencies[n] = depe

    for n, r in dependencies.items():
        if n in r: 
            # print(f"{c} Loop: {n} {r}")
            assert False

    final_vals = {i:None for i in nodes}
    
    def calc(x):
        if final_vals[x]is not None: return final_vals[x]
        if x not in mod_conn:
            assert x in ini
            final_vals[x] = ini[x]
            return final_vals[x]
        l,r,op = mod_conn[x]
        ll = calc(l)
        rr = calc(r)
        opp = {
            "AND":and_,
            "OR":or_,
            "XOR":xor,
        }[op]
        final_vals[x] = opp(ll, rr)
        return final_vals[x]

    return (swaps, xi, yi, [calc(f'z{i:02}') for i in range(46)]) 

import random
def list_to_bin(l):
    s = 0
    c = 1
    for i in l:
        s += i * c
        c <<= 1
    return s

def check(swps, n=46):
    xi = [random.randint(0,1) for _ in range(n)]
    yi = [random.randint(0,1) for _ in range(n)]
    _,_,_,res = check_addition(xi, yi, swps)
    return list_to_bin(res) == list_to_bin(xi) + list_to_bin(yi)

#### THEN BINARY SEARCH USING THIS TO FIND THE LOWEST BIT WITH A MISWIRING

assert all(check(
 {"z07":"nqk", "fgt":"pcp", "z24":"fpq","srn":"z32"},
 45
) for _ in range(500))
aoc_helper.lazy_submit(day=24, year=2024, solution=part_one, data=data)
