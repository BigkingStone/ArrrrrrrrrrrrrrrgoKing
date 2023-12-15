import sys
input = sys.stdin.readline
k, l = list(map(int, input().strip().split()))
arr = list(reversed([input().strip() for _ in range(l)]))
ans = []
s = set()
for i in range(l):
  if arr[i] in s: continue
  ans.append(arr[i])
  s.add(arr[i])
ans.reverse()
size = len(ans)
for i in range(k):
  if i >= size: break
  print(ans[i])
