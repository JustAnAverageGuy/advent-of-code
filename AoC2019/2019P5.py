with open(r'AoC2019\AoC2019_Day5_input.txt', 'r') as f:
    I = list(map(int, f.read().strip().split(',')))


def run(code, inputs=[1]):
    ptr = 0  # instruction pointer
    f = 1  # error flag
    outputs = []
    while code[ptr] != 99:
        if int(str(code[ptr])[-2:]) == 1:  # opcode 1 : 1 a b c -> memory[c] = a + b
            opcode = '0'*(5-len(str(code[ptr])))+str(code[ptr])[:-2]
            code[code[ptr + 3]] = (code[code[ptr+1]] if opcode[-1] == '0' else code[ptr + 1]) + (
                code[code[ptr+2]] if opcode[-2] == '0' else code[ptr + 2])
            ptr += 4
        elif int(str(code[ptr])[-2:]) == 2:  # opcode 2 : 2 a b c -> memory[c] = a * b
            opcode = '0'*(5-len(str(code[ptr])))+str(code[ptr])[:-2]
            code[code[ptr + 3]] = (code[code[ptr+1]] if opcode[-1] == '0' else code[ptr + 1]) * (
                code[code[ptr+2]] if opcode[-2] == '0' else code[ptr + 2])
            ptr += 4
        elif int(str(code[ptr])[-2:]) == 3:  # store input
            code[code[ptr + 1]] = inputs[0]  # for part 1
            ptr += 2
        elif int(str(code[ptr])[-2:]) == 4:  # store output
            # print(code[code[ptr + 1]])  # output
            outputs.append(code[code[ptr + 1]])
            ptr += 2
        elif int(str(code[ptr])[-2:]) == 5:  # jump-if-true
            opcode = '0'*(4-len(str(code[ptr])))+str(code[ptr])[:-2]
            if (code[ptr+1] if opcode[-1] == '1' else code[code[ptr+1]]) != 0:
                ptr = (code[ptr+2] if opcode[-2] == '1' else code[code[ptr+2]])
            else:
                ptr += 3
        elif int(str(code[ptr])[-2:]) == 6:  # jump-if-false
            opcode = '0'*(4-len(str(code[ptr])))+str(code[ptr])[:-2]
            if (code[ptr+1] if opcode[-1] == '1' else code[code[ptr+1]]) == 0:
                ptr = (code[ptr+2] if opcode[-2] == '1' else code[code[ptr+2]])
            else:
                ptr += 3
        elif int(str(code[ptr])[-2:]) == 7:  # less than
            opcode = '0'*(5-len(str(code[ptr])))+str(code[ptr])[:-2]
            code[code[ptr + 3]] = 1 if (code[code[ptr+1]] if opcode[-1] == '0' else code[ptr+1]) < (
                code[code[ptr+2]] if opcode[-2] == '0' else code[ptr+2]) else 0
            ptr += 4
        elif int(str(code[ptr])[-2:]) == 8:  # equality
            opcode = '0'*(5-len(str(code[ptr])))+str(code[ptr])[:-2]
            code[code[ptr + 3]] = 1 if (code[code[ptr+1]] if opcode[-1] == '0' else code[ptr+1]) == (
                code[code[ptr+2]] if opcode[-2] == '0' else code[ptr+2]) else 0  # can simplify booleans but whatever
            ptr += 4
        else:
            f = 0
            break
    return outputs if f else 'error'


print(run(I, [5]))
