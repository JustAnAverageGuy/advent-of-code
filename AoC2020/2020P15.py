with open("AoC2020_Day15_input.txt", 'r') as file:
    elvmemory = list(map(int, file.read().split(',')))


# part 1
""" seq = elvmemory
for _ in range(2100):
    if seq[-1] not in seq[:-1]:
        seq.append(0)
    else:
        p = 2
        q = seq[-1]
        while True:
            if seq[-p] == q:
                seq.append(p-1)
                break
            p += 1

print(seq[2019]) """

# part 2
seq = elvmemory
seqcumul = {i: elvmemory.index(i) for i in elvmemory}
for step in range(3*(10**7) + 100):
    if seq
    if seq[-1] in seqcumul:
        pass
    else:
        seqcumul[seq[-1]] = len(seq) - 1
