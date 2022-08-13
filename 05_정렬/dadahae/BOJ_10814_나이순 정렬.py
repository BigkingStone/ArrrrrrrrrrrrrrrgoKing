N = int(input())
arr = []
temp = []
for i in range(N):
  arr.append(list(input().split()))
  temp.append( [0, ""] )
  arr[i][0] = int(arr[i][0])

def merge_sort(st:int, en:int):
  if en == st+1:
    return 
  mid = (st+en) // 2
  merge_sort(st, mid)
  merge_sort(mid, en)
  merge(st, en)

def merge(st:int, en:int):
  mid = (st+en) // 2
  lidx = st
  ridx = mid
  for i in range(st, en):
    if lidx == mid:
      temp[i] = arr[ridx]
      ridx += 1
    elif ridx == en:
      temp[i] = arr[lidx]
      lidx += 1
    elif arr[lidx][0] <= arr[ridx][0]:
      temp[i] = arr[lidx]
      lidx += 1
    else:
      temp[i] = arr[ridx]
      ridx += 1
  for i in range(st,en):
    arr[i] = temp[i]

merge_sort(0, N)
for i in range(N):
  print( " ".join(map(str, arr[i])) )
