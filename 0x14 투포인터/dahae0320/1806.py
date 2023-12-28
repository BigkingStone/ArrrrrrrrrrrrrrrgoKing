import sys
input = sys.stdin.readline
n, s = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
st = 0; en = 0
tot = 0
mi = 0x7ffffff
while st < n:
  while en < n and arr[en] + tot < s:
    tot += arr[en]
    en += 1
  if en == n: break
  mi = min(mi, en-st+1)
  tot -= arr[st]
  st += 1
if mi == 0x7ffffff: mi = 0
print(mi)
