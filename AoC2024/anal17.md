
program:
  0 1 2 3 4 5 6 7 8 9 a b c d e f
  2,4,1,1,7,5,1,5,4,0,0,3,5,5,3,0

2,4 -> B = A % 8
1,1 -> B ^= 1 
7,5 -> C = (A >> B)
1,5 -> B ^= 5
4,0 -> B ^= C
0,3 -> A >>= 3
5,5 -> out B & 8
3,0 -> if A > 0: goto start

for a; k = (a&7); out.append(
  ((a >> (k^1)) & 7) ^ k ^ 4
)

## solution: build it digit by digit in reverse order
