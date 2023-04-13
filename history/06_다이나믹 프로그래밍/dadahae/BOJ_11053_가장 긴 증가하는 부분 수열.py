N = int(input())
num = list(map(int, input().split()))
d = [1]*N
for i in range(N):
  for j in range(i):
    if num[i] > num[j]:
      d[i] = max(d[i], d[j]+1)
print(max(d))
