from bisect import bisect_left
import sys
input = sys.stdin.readline

def solve(arr, target, m):
  idx = bisect_left(arr, target)
  cnt = 0
  for i in range(idx, len(arr)):
    cnt += arr[i] // target
  return cnt >= m

m, n = list(map(int, input().strip().split()))
arr = sorted(list(map(int, input().strip().split())))
k = sum(arr)
st = 1
en = k  # 최대 1000000000
mx = 0  # 최대 막대 길이
while st < en:
  mid = (st+en+1) // 2
  if mid * m > k:
    en = mid - 1
  elif solve(arr, mid, m):
    st = mid
    mx = max(mx, mid)
  else:
    en = mid - 1
if solve(arr, (st+en+1)//2, m):
  mx = max(mx, (st+en+1)//2)
print(mx)
