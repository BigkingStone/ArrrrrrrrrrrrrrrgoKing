N = int(input())
d = [0]*N
num = [0]*N
for i in range(N): num[i] = int(input())
num.sort()
for i in range(N):
  d[i] = num[i]*(N-i)

print(max(d))
