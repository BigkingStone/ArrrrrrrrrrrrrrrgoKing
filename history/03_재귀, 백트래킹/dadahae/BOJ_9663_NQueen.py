def NQueen(cur):
  if cur == n:
    global result
    result += 1
    return
  
  for i in range(n):
    if issued[i] == False and issued2[cur+i] == False and issued3[i-cur-(n-1)] == False:
      answer[cur] = i
      issued[i] = True
      issued2[cur+i] = True
      issued3[i-cur-(n-1)] = True
      NQueen(cur+1)
      issued[i] = False
      issued2[cur+i] = False
      issued3[i-cur-(n-1)] = False

n = int(input())
result = 0
issued = [False]*n
issued2 = [False]*(2*n -1)  # 대각선의 개수
issued3 = [False]*(2*n -1)
answer = [-1]*n
NQueen(0)
print(result)

## Python으로는 시간초과가 떠서 Pypy3로 채점을 통과하였다.
