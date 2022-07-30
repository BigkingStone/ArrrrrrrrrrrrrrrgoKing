from collections import deque

n, m = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
area_max = 0
pic = 0

board = []
for i in range(n):
    board.append( list(map(int, input().split())) )

def BFS(a, b) -> int:
  area = 0
  q = deque([[a,b]])
  board[a][b] = 0 # 방문함
  area += 1
  while q:
    item = q.popleft()
    for i in range(4):
      nx = item[0] + dx[i]
      ny = item[1] + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if board[nx][ny] == 0:
        continue
      board[nx][ny] = 0
      area += 1
      q.append([nx,ny])
  return area

for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      area = BFS(i, j)
      pic += 1
      if area > area_max:
        area_max = area

print(pic, area_max, sep="\n")
