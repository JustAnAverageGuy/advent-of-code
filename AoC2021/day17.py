"""
import re
with open("input17.txt", 'r') as file:
    a = re.match(
        r'target area: x=([\d\-]*)..([\d\-]*), y=([\d\-]*)..([\d\-]*)', file.read())
    xmin, xmax, ymin, ymax = map(int, a.group(1, 2, 3, 4))
"""
xmin, xmax, ymin, ymax = 209, 238, -86, -59


def simulate(vx: int, vy: int):
    sx, sy = 0, 0
    while vx:
        sx += vx
        sy += vy
        vx -= 1
        vy -= 1
