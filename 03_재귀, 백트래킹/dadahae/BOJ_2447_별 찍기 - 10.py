N = int(input())
board = [[" " for _ in range(N)] for _ in range(N)]

def solve(x,y,k):
  if k == 1:
    board[x][y] = "*"
    return
  tri = k // 3 
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        continue
      solve(x + tri*i, y + tri*j, tri)

solve(0,0,N)

for i in range(N):
  print("".join(board[i]))
