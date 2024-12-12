def nex(uniq):
    nxt = set()
    for n in uniq:
        if n == 0: nxt.add(1)
        elif len(str(n)) % 2 == 0:
            s = str(n)
            r,l = s[len(s)//2:],s[:len(s)//2]
            nxt.add(int(r))
            nxt.add(int(l))
        else:
            nxt.add(2024 * n)
    return nxt

uniq = {19956,19957}

def simulate(start):
    i = 0
    while True:
        ne = nex(start)
        if start == ne: return (i, start)
        i += 1
        start = ne


print(len(simulate(start=uniq)[1]))
