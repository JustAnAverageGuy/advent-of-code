with open(r"AoC2019\AoC2019_Day2_input.txt", 'r') as f:
    I = list(map(int, f.read().strip().split(',')))


def run(code):
    ptr = 0
    f = 1
    while code[ptr] != 99:
        if code[ptr] == 1:
            code[code[ptr + 3]] = code[code[ptr+1]] + code[code[ptr+2]]
            ptr += 4
        elif code[ptr] == 2:
            code[code[ptr + 3]] = code[code[ptr+1]] * code[code[ptr+2]]
            ptr += 4
        else:
            f = 0
            break
    return code[0] if f else 'error'


#print(run([I[0], 12, 2]+I[3:]))

for a in range(100):
    for b in range(100):
        t = run([I[0], a, b]+I[3:])
        if t == 19690720:
            print(100*a+b)
