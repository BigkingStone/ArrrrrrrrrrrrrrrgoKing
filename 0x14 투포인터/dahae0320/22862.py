import sys
input = sys.stdin.readline
n, k = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
en = 0
ans = 0
tmp = 0
cnt = k
for st in range(n):
  while en < n:
    # print(f"st: {st}, en: {en}, tmp: {tmp}, ans: {ans}")
    if arr[en] % 2 != 0:  # arr[en]이 홀수일 때
      if cnt - 1 == -1: break
      cnt -= 1
    else:   # arr[en]이 짝수일 때
      tmp += 1
    ans = max(tmp, ans) if cnt == 0 else ans
    en += 1
  if en >= n: break
  if arr[st] % 2 != 0 and cnt < k: cnt += 1
  else: tmp -= 1
print(ans)
