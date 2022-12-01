with open("AoC2020_Day5_input.txt", 'r') as file:
    seatIDsInLetters = file.read().split()

# print(max(seatIDs), min(seatIDs))
seatIDs = []
for i in seatIDsInLetters:
    hmmm = '0b'
    for j in i:
        if j == 'B' or j == 'R':
            hmmm += '1'
        else:
            hmmm += '0'
    seatIDs.append(int(hmmm, 2))


i = 56
while i <= 935:
    if (i not in seatIDs) and (i - 1 in seatIDs) and (i + 1 in seatIDs):
        print(i)
    i += 1
# print(len(seatIDs))
print(max(seatIDs))
