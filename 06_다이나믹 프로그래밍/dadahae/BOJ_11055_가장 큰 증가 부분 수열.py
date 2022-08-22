N = int(input())
d = [0]*(N)
s = list(map(int, input().split()))
for i in range(N):
  d[i] = s[i]

for i in range(N):
  for j in range(0,i):
    if s[i] > s[j]:
      d[i] = max(d[i], d[j]+s[i])

print(max(d))
