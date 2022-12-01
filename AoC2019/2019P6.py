with open(r'AoC2019\AoC2019_Day6_input.txt', 'r') as f:
    orbits = [tuple(i.strip().split(')')) for i in f.readlines()]

orbit_map = dict().fromkeys(map(lambda x: x[0], orbits), [])

for i in orbits:
    orbit_map[i[0]].append(i[1])
