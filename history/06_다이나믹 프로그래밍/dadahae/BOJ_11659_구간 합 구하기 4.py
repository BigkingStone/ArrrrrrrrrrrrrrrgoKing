import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
d = [0] + list(map(int, input().split()))
for i in range(1,N+1):
  d[i] = d[i-1] + d[i]
for _ in range(M):
  i, j = map(int, input().split())
  print(d[j]-d[i-1])
