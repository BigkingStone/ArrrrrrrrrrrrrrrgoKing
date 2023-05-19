N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
isused = [False for _ in range(N)]
arr = [-1 for _ in range(M)]

def nm(k):
  if k == M:
    print(" ".join(map(str, arr)))
    return
  for i in range(N):
    if isused[i]: continue
    if i != 0 and nums[i-1] == nums[i] and not isused[i-1]: continue
    arr[k] = nums[i]
    isused[i] = True
    nm(k+1)
    isused[i] = False

nm(0)
