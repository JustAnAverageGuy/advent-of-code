with open("input7.txt", 'r') as file:
    crabs = list(map(int, file.readline().split(',')))

# crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
# print(sum(crabs)/len(crabs))


def answer(crabs):
    medans = 0
    menans = 0
#    median = sorted(crabs)[len(crabs)//2]
    mean = round(sum(crabs)/len(crabs))-1
    for i in crabs:
        #        medans += 0.5 * abs(i - median)*(abs(i - median) + 1)
        menans += 0.5 * abs(i - mean)*(abs(i - mean) + 1)
    return medans, menans


# engineer induction
print(answer(crabs))
