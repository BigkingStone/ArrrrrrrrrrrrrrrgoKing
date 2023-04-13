def NandM(k:int):
  if k == M:
    print( " ".join(list(map(str, answer))) )
  else:
    for i in range(1, N+1):
      answer[k] = i
      NandM(k+1)

N, M = map(int, input().split())
answer = [0]*M
NandM(0)
