t = int(input())
for i in range(t):
  n, m = list(map(int, input().strip().split()))
  a = sorted(list(map(int, input().strip().split())), reverse=True)
  b = sorted(list(map(int, input().strip().split())), reverse=True)
  aidx = 0
  bidx = 0
  cnt = 0
  for _ in range(n+m):
    if aidx == n:
      bidx += 1
    elif bidx == m:
      aidx += 1
    elif a[aidx] > b[bidx]:
      aidx += 1
      cnt += m - bidx
    else:
      bidx += 1
  print(cnt)
