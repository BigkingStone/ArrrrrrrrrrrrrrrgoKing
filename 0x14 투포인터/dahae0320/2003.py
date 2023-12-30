import sys
input = sys.stdin.readline
n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
tot = arr[0]
cnt = 0
en = 0
for st in range(n):
  while en+1 < n and tot < m:
    en += 1
    tot += arr[en]
  if en == n: break
  if tot == m: cnt += 1
  tot -= arr[st]
print(cnt)
