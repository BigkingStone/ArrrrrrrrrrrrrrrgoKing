import sys
input = sys.stdin.readline
n = int(input())
t = [-1 for _ in range(n+1)]
p = [-1 for _ in range(n+1)]
for i in range(1, n+1):
  t[i], p[i] = list(map(int, input().strip().split()))
d = [0 for _ in range(n+2)]
for i in range(n, 0, -1):
  if t[i]+i-1 <= n:
    d[i] = max(d[i+t[i]] + p[i], d[i+1])
  else:
    d[i] = d[i+1]
print(max(d))
