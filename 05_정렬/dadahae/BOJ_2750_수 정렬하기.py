def merge_sort(st:int, en:int):
  if en == st+1:
    return
  mid = (st+en) // 2
  merge_sort(st,mid)
  merge_sort(mid,en)
  merge(st,en)

def merge(st:int, en:int):
  mid = (st+en) // 2
  lidx = st
  ridx = mid
  for i in range(st, en):
    if ridx == en:
      temp[i] = arr[lidx]
      lidx += 1
    elif lidx == mid:
      temp[i] = arr[ridx]
      ridx += 1
    elif arr[lidx] <= arr[ridx]:
      temp[i] = arr[lidx]
      lidx += 1
    else:
      temp[i] = arr[ridx]
      ridx += 1
  for i in range(st, en):
    arr[i] = temp[i]

arr = [0]*10001
temp = [0]*10001

N = int(input())
for i in range(N):
  arr[i] = int(input())

merge_sort(0,N)

print(" ".join(map(str, arr[:N])))
