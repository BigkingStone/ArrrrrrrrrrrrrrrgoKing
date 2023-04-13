N = int(input())
num = list(map(int, input().split()))
d1 = [1]*N
d2 = [[num[i]] for i in range(N)]
for i in range(N):
  for j in range(i):
    if num[i] > num[j]:
      d1[i] = max(d1[i], d1[j]+1)
      d2[i] = d2[i] if d1[i] > d1[j]+1 else d2[j] + [num[i]]
print(max(d1))
idx = d1.index(max(d1))
print(" ".join(map(str, d2[idx])))
