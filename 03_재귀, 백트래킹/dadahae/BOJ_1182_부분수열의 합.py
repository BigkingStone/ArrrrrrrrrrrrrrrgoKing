def sumOfSubsequence(k: int, cur: int):
  global cnt
  if k == N:
    if cur == S:
      cnt += 1
    return
  sumOfSubsequence(k+1, cur)
  sumOfSubsequence(k+1, cur+seq[k])

N, S = map(int, input().split())
cnt = 0
seq = list(map(int, input().split()))

sumOfSubsequence(0, 0)
if S == 0:
  print(cnt-1)
else: 
  print(cnt)
