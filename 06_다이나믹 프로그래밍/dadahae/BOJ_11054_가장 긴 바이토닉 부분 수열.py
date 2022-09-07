N = int(input())
s = list(map(int, input().split()))
DL = [1]*N
DR = [1]*N
D = [0]*N
for i in range(N):
  lidx = i
  ridx = (N-1)-i
  for j in range(lidx):
    if s[lidx] > s[j]:
      DL[lidx] = max(DL[lidx], DL[j]+1)
  for j in range(N-1, ridx, -1):
    if s[ridx] > s[j]:
      DR[ridx] = max(DR[ridx], DR[j]+1)
for i in range(N):
  D[i] = DL[i] + DR[i] - 1
print(max(D))
