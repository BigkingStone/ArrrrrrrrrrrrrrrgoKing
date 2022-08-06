def foo(n:int, a:int, b:int):
  global answer
  if isAllSame(n,a,b):
    answer += str(board[a][b])
  else:
    half = n // 2
    answer += "("
    foo(half, a, b)
    foo(half, a, b+half)
    foo(half, a+half, b)
    foo(half, a+half, b+half)
    answer += ")"

def isAllSame(n:int, a:int, b:int):
  for x in range(a, a+n):
    for y in range(b, b+n):
      if board[x][y] != board[a][b]:
        return False
  return True

N = int(input())
answer = ""
board = []
for i in range(N):
  board.append( list(map(int, input())) )

foo(N, 0, 0)
print(answer)
