from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
table = [[0 for _ in range(7)] for _ in range(2)]
answer = 0

for _ in range(N):
  S, Y = map(int, input().split())
  table[S][Y] += 1

for s in range(2):
  for y in range(1,7):
    if table[s][y] == 0: continue
    answer += table[s][y] // K
    answer += 1 if table[s][y] % K != 0 else 0

print(answer)
