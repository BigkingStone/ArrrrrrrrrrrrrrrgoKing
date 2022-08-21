N = int(input())
d = list(map(int, input().split()))
for i in range(1, N):
  d[i] = max(d[i], d[i-1] + d[i])
max_n = max(d)
print(max_n)
