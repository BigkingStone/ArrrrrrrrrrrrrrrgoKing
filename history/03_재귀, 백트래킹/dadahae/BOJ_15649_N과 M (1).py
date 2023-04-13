def NandM(k: int):
  if k == M:
    for i in range(M):
      print(answer[i], end=" ")
    print()
    return

  for i in range(1, N+1):
    if issued[i] == False:
      answer[k] = i
      issued[i] = True
      NandM(k+1)
      issued[i] = False

N, M = map(int, input().split())
issued = [False]*(N+1)
answer = [0]*M
NandM(0)
