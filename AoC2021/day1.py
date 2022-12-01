with open("input1.txt", "r") as file:
    depths = [int(i.strip()) for i in file.readlines()]

""" cnt = 0
for i in range(len(depths)-1):
    if depths[i+1] - depths[i] > 0:
        cnt += 1
print(cnt)
 """
# Part 2

ThreeSlidingWindow = [depths[i] + depths[i+1] + depths[i+2]
                      for i in range(len(depths) - 2)]

cnt = 0
for i in range(len(ThreeSlidingWindow)-1):
    if ThreeSlidingWindow[i+1] - ThreeSlidingWindow[i] > 0:
        cnt += 1
print(cnt)
