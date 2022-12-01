with open("AoC2022\\input_1.txt") as f:
    calories = [sum(map(int, i.split())) for i in f.read().split('\n\n')]
print(sum(sorted(calories)[-3:]))
