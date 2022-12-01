from functools import reduce

with open("input10.txt", 'r') as file:
    brackets = [i.strip() for i in file.readlines()]


def analysis(synt):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    stack = []
    for j in synt:
        if j in opening:
            stack.append(j)
        elif closing[opening.index(stack.pop())] != j:
            return (True, j)
    return (False, ''.join(stack))


""" 
sm = 0
score = {')': 3, "]": 57, "}": 1197, ">": 25137}
for i in brackets:
    q = analysis(i)
    if q[0]:
        sm += score[q[1]]
print(sm)
 """

incomplete = [analysis(i)[1] for i in brackets if not analysis(i)[0]]


def closed(i):
    ans = ''
    for j in i[::-1]:
        if j == '(':
            ans += ')'
        if j == '[':
            ans += ']'
        if j == '{':
            ans += '}'
        if j == '<':
            ans += '>'
    return ans


scores = [reduce(lambda x, y: 5*x + {')': 1, ']': 2, '}': 3,
                 '>': 4}.get(y), closed(i), 0) for i in incomplete]
print(sorted(scores)[len(scores)//2])
