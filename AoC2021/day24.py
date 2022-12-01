with open("input24.txt", 'r') as file:
    monad = [tuple(i.strip().split()) for i in file.readlines()]


def mona(model: str, prog: list[tuple[str, ...]] = monad):
    ar = {"w": 0, "x": 0, "y": 0, "z": 0}
    k = 0
    for i in prog:
        if i[0] == "inp":
            ar[i[1]] = int(model[k])
            k += 1
        elif i[0] == "mul":
            ar[i[1]] *= ar[i[2]] if i[2] in ar else int(i[2])
        elif i[0] == "add":
            ar[i[1]] += ar[i[2]] if i[2] in ar else int(i[2])
        elif i[0] == "div":
            ar[i[1]] = int(ar[i[1]] / (ar[i[2]] if i[2] in ar else int(i[2])))
        elif i[0] == "mod":
            ar[i[1]] %= ar[i[2]] if i[2] in ar else int(i[2])
        else:  # Equal Case
            ar[i[1]] = int(ar[i[1]] == (ar[i[2]] if i[2] in ar else int(i[2])))
    return not(ar["z"])  # 1 if valid , 0 if invalid
