import sys
input = sys.stdin.readline
N, M, L = list(map(int, input().split()))
arr = sorted(list(map(int, input().split()))+[0,L]) if N != 0 else [0,L]

def solve():
  st = 1
  en = L
  while (st < en):
    mid = (st+en) // 2
    new = 0
    for i in range(1, N+2):
      if arr[i] - arr[i-1] > mid:
        new += (arr[i] - arr[i-1] - 1) // mid
    if new <= M:
      en = mid
    else:
      st = mid + 1
  return st
      
ans = solve()
print(ans)
