from collections import deque

def BFS1(x: int, y: int, color: str):
  q = deque([[x,y]])
  visited1[x][y] = True
  while q:
    item = q.popleft()
    x = item[0]; y = item[1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if board[nx][ny] != color or visited1[nx][ny]:
        continue
      visited1[nx][ny] = True
      q.append([nx,ny])

def BFS2(x: int, y: int, color: str):
  q = deque([[x,y]])
  visited2[x][y] = True
  while q:
    item = q.popleft()
    x = item[0]; y = item[1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if visited2[nx][ny]:
        continue
      if (color == 'B' and board[nx][ny] == 'B') or (color in ['R','G'] and board[nx][ny] in ['R','G']):
        visited2[nx][ny] = True
        q.append([nx,ny])

N = int(input())
board = []
visited1 = []
visited2 = []
result1 = 0
result2 = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(N):
  line = input()
  board.append( [l for l in line] )
  visited1.append( [False]*N )
  visited2.append( [False]*N )

for i in range(N):
  for j in range(N):
    if visited1[i][j] == False:
      BFS1(i,j, board[i][j])
      result1 += 1
    if visited2[i][j] == False:
      BFS2(i,j, board[i][j])
      result2 += 1

print(result1, result2)
