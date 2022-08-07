def NandM(k:int):
  if k == M:
    print( " ".join(list(map(str, answer))) )
  else:
    st = 1
    if k != 0: st = answer[k-1] + 1
    for i in range(st, N+1):
      if isused[i] == False:
        answer[k] = i
        isused[i] = True
        NandM(k+1)
        isused[i] = False


N, M = map(int, input().split())
answer = [0]*(M)
isused = [False]*(1+N)
NandM(0)
