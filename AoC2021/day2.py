with open("input2.txt", 'r') as file:
    directions = [i.strip().split() for i in file.readlines()]

print(directions)


x = 0
depth = 0
""" for i in directions:
    if i[0][0] == 'f':
        x += int(i[1])
    elif i[0][0] == 'd':
        depth += int(i[1])
    else:
        depth -= int(i[1])
print(x, depth, x*depth)
 """
# Part 2

aim = 0
for i in directions:
    if i[0][0] == 'f':
        x += int(i[1])
        depth += aim * int(i[1])
    elif i[0][0] == 'd':
        aim += int(i[1])
    else:
        aim -= int(i[1])
print(x, depth, x*depth)
