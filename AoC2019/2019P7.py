from itertools import permutations


with open(r'AoC2019\AoC2019_Day7_input.txt', 'r') as f:
    I = list(map(int, f.read().strip().split(',')))


def run(code, inputs=[1],ptr=0):
    f = 1  # error flag
    k = 0
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
            if k < len(inputs):
                code[code[ptr + 1]] = inputs[k]  # for part 1
                k += 1
                ptr += 2
            else:
                return (2,outputs,code,ptr)# WTFFFFFF
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
    return (f,outputs) # f== 1 : daijobu, f == 0 : error , f== 2: waiting for input


""" 
class Intcode:
    def __init__(self,inputs,code=I) -> None:
        self.inputs = inputs
        self.code = code
        self.ptr = 0
        self.flag = 1 # not-error flag
        self.k = 0
        self.outputs = []
    def run(self):
        while self.code[self.ptr] !=99
        

 """
phases = permutations(range(5, 10))
thrusts = []


for i in phases:
    k = run(I, [i[0], 0])
    a = k[1][0]
    for k in range(1, 5):
        a = run(I, [i[k], a])[0]
    thrusts.append(a)


# print(max(thrusts))
