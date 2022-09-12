N, M = map(int, input().split())
num = sorted(list(map(int,input().split())))
arr = [0]*(M) 

def func(k):
  if k == M:
    print(" ".join(map(str,arr)))
  else:
    idx = 0
    if k != 0: idx = num.index(arr[k-1]) + 1
    for i in range(idx, N):
      arr[k] = num[i]
      func(k+1)

func(0)
