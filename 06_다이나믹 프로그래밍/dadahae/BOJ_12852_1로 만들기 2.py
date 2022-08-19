import sys
input = sys.stdin.readline

N = int(input().rstrip())
d = [0]*(N+1)
p = [ [1] for _ in range(N+1) ]

for i in range(2, N+1):
  d[i] = d[i-1] + 1
  idx = i-1
  if i%2 == 0:
    idx = idx if d[i//2]+1 > d[i] else i//2
    d[i] = min(d[i//2]+1, d[i])
  if i%3 == 0:
    idx = idx if d[i//3]+1 > d[i] else i//3
    d[i] = min(d[i//3]+1, d[i])
  p[i] = p[idx] + [i]

print(d[N])
print(" ".join(map(str, p[N][::-1])))
