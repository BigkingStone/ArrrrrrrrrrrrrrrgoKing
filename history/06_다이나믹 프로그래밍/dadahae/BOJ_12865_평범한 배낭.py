N, K = map(int, input().split())
d = [[0 for _ in range(K+1)] for _ in range(N+1)]
val = [0]*(N+1)
wei = [0]*(N+1)
for i in range(1,N+1):
  wei[i], val[i] = map(int, input().split())

ans = 0
for i in range(1, N+1):
  for w in range(1, K+1):
    if wei[i] > w:
      d[i][w] = d[i-1][w]
    else:
      d[i][w] = max(val[i]+d[i-1][w-wei[i]], d[i-1][w])
  ans = max(d[i])
print(ans)
