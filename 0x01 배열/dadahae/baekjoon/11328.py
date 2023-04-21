N = int(input())

# test case
for _ in range(N):
  original, compare = map(list, input().split())
  compareSize = len(compare)
  for ori in original:
    if ori in compare:
      compare.pop(compare.index(ori))
      
  if len(original) == compareSize and len(compare) == 0:
    print("Possible")
  else: 
    print("Impossible")
