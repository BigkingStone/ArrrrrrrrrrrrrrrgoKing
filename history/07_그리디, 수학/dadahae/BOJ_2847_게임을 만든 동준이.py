N = int(input())
level = [0]*(N+1)
cnt = 0
for i in range(1,N+1):
  level[i] = int(input())
for i in range(N, 1, -1):
  if level[i] <= level[i-1]:
    cnt += level[i-1] - level[i] + 1
    level[i-1] -= level[i-1] - level[i] + 1
print(cnt)
