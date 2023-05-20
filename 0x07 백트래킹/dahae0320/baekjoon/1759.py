L, C = map(int, input().split())
alpha = sorted(list(input().split()))
isused = [False for _ in range(C)]
arr = ['' for _ in range(L)]

def password(k, cnt):
  if k == L:
    if cnt >= 1 and L - cnt >= 2:
      print("".join(arr))
    return
  st = alpha.index(arr[k-1]) + 1 if k != 0 else 0
  for i in range(st, C):
    if not isused[i]:
      arr[k] = alpha[i]
      isused[i] = True
      if alpha[i] in ['a','e','i','o','u']:
        password(k+1, cnt+1)
      else:
        password(k+1, cnt)
      isused[i] = False

password(0,0)
