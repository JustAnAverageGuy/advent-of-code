with open(r'AoC2020_Day8_input.txt', 'r') as file:
    code = list(map(lambda x: x.strip(), file.readlines()))

with open(r'input.txt', 'r') as file:
    smallcode = list(map(lambda x: x.strip(), file.readlines()))

# PART 1
""" def runCode(code):
    visited = []
    i = 0
    accumulation = 0
    while True:
        if i in visited:
            return accumulation
        if code[i][0] == 'n':
            visited.append(i)
            i += 1
        elif code[i][0] == 'a':
            accumulation += int(code[i][4:])
            visited.append(i)
            i += 1
        else:
            visited.append(i)
            i += int(code[i][4:])


print(runCode(code))
 """


def isLoop(code):
    visited = []
    i = 0
    accumulation = 0
    while True:
        if i in visited:
            return True, accumulation

        if code[i][0] == 'n':
            visited.append(i)
            i += 1
        elif code[i][0] == 'a':
            accumulation += int(code[i][4:])
            visited.append(i)
            i += 1
        else:
            visited.append(i)
            i += int(code[i][4:])

        if i not in range(0, len(code)):
            return False, accumulation


def ChangeCulprit(code):
    saved = code
    for i in range(len(code)):
        if code[i][0] == 'n':
            code[i] = code[i].replace('nop', 'jmp')
            if not isLoop(code)[0]:
                return isLoop(code)[1]
            else:
                code = saved
        if code[i][0] == 'j':
            code[i] = code[i].replace('jmp', 'nop')
            if not isLoop(code)[0]:
                return isLoop(code)[1]
            else:
                code = saved

# SOMETHING WRONG SOMEWHERE CHECK PLEASE, ACTUALLY SOMEWHERE IN isLoop()


print(ChangeCulprit(smallcode))

# print(isLoop(smallcode))
