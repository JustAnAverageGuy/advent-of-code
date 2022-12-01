with open("input21.txt", 'r') as file:
    play1 = int(file.readline()[-2])
    play2 = int(file.readline()[-1])


hmm = {i: i for i in range(1, 10)}
hmm[0] = 10


""" def game(pos1: int = play1, pos2: int = play2):
    steps = 0
    score1, score2 = 0, 0
    while True:
        steps += 1
        pos1 = hmm[(pos1 + (-steps-3)) % 10]
        score1 += pos1
        if score1 >= 1000:
            return score2 * 3 * steps
        steps += 1
        pos2 = hmm[(pos2 + (-steps-3)) % 10]
        score2 += pos2
        if score2 >= 1000:
            return score1 * 3 * steps """

initial1 = {i: 0 for i in range(1, 11)}
initial2 = {i: 0 for i in range(1, 11)}
initial1[play1], initial2[play2] = 1, 1
# three roll sum : number of universes with that sum
universes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


# current = {1:0,2:1,3:0,4:0,5:0,6:0,7:0,8:1,9:0,10:0}
# nex(current) = {1:,2:,3:,4:,5:1,6:3,7:,8:,9:,10:}
def nex(current: dict[int, int]):
    new = {i: 0 for i in range(1, 11)}
    for i in current:
        for j in universes:
            new[hmm[(i + j) % 10]] += current[i] * universes[j]
    return new


print(nex(initial1))


def diracgame():
    pass


print(diracgame())
