N, M = map(int, input().split())
arr = [0]*(M)
isused = [False]*(N+1)

def func(k):
  if k == M:
    print( " ".join(map(str, arr)) )
  else:
    idx = 1
    if k != 0: idx = arr[k-1]
    for i in range(idx, N+1):
      arr[k] = i
      func(k+1)

func(0)
