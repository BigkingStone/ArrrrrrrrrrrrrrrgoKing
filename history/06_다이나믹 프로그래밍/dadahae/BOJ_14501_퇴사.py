N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
D = [0]*(N+1)
for i in range(1,N+1):
  T[i], P[i] = map(int, input().split())
  if T[i]+i <= N+1:
    D[i] = P[i]
for i in range(1,N+1):
  for j in range(1, i):
    if i >= (T[j]+j) and N+1 >= (T[i]+i):
      D[i] = max(D[j]+P[i], D[i])
print(max(D))
