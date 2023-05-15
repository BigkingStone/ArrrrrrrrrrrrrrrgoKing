N = int(input())
board = [ [" " for _ in range(N*2-1)] for _ in range(N) ]

def solve(x,y,n):
  if n == 3:
    star(x,y)
    return
  tri = n // 2
  solve(x+tri, y, tri)
  solve(x, y+tri, tri)
  solve(x+tri, y+tri*2, tri)

def star(x,y):
  for i in range(3):
    for j in range(5):
      if i == 0 and (j == 0 or j == 1 or j == 3 or j == 4): continue
      if i == 1 and (j == 0 or j == 2 or j == 4): continue
      board[x+i][y+j] = "*"

solve(0,0,N)

for i in range(N):
  print("".join(map(str, board[i])))
