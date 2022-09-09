N, M = map(int, input().split())
arr = [0]*M    # 0-indexed
isused = [0]*(N+1)    # 1-indexed
num = [0] + list(map(int, input().split()))    # 1-indexed
num.sort()

def func(k):
  if k == M:
    print(" ".join(map(str, arr)))
  else:
    for i in range(1, N+1):
      if isused[i] == False:
        arr[k] = num[i]
        isused[i] = True
        func(k+1)
        isused[i] = False

func(0)
