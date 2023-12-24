import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
mi = 3000000001
ans = []
for i in range(n):
  st = i+1
  en = n-1
  while st <= en:
    mid = (st+en) // 2
    tmp = arr[i] + arr[mid]
    if abs(tmp) < abs(mi):  
      mi = tmp
      ans = [arr[i], arr[mid]]
    if tmp > 0: en = mid - 1
    elif tmp < 0: st = mid + 1
    else: break
print(" ".join(map(str, ans)))
