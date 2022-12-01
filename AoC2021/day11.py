import numpy as np
with open("input11.txt", 'r') as file:
    x = np.genfromtxt(file, dtype=int, delimiter=1)


def nex(octopi):
    dirn = [(i, j) for i in range(-1, 2)
            for j in range(-1, 2) if not (i == j == 0)]
    padocto = np.pad(octopi, pad_width=1, mode='constant', constant_values=-10)
    padocto += 1
    flashed = np.zeros_like(padocto, dtype=int)
    while (True in (padocto > 9)):
        for index, energy in np.ndenumerate(padocto):
            if 0 < index[0] < len(padocto)-1 and 0 < index[1] < len(padocto[0]) - 1:
                if energy > 9 and not(flashed[index]):
                    flashed[index] = 1
                    for k in dirn:
                        padocto[index[0]+k[0], index[1]+k[1]
                                ] += 1 if not(flashed[index[0]+k[0], index[1]+k[1]]) else 0
                    padocto[index] = 0
    return padocto[1:-1, 1:-1], np.count_nonzero(flashed)


cnt = 0
for i in range(1000):
    x, p = nex(x)
    if p == 100:
        print(i+1)

# BHery Ugli kode
# Pliz klin
