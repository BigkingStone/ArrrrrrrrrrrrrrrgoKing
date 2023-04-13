from collections import deque

def fire():
  w, h = map(int, input().split())
  board = []
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  q1 = deque(); visited1 = []
  q2 = deque(); visited2 = []

  for i in range(h):
    board.append( list(map(str, input())) )
    visited1.append( [-1]*w ) # 불이 방문한 시각을 나타내는 배열
    visited2.append( [-1]*w ) # 상근이가 방문한 시각을 나타내는 배열 (불의 방문 시각에 영향을 받음)
    for j in range(w):
      if board[i][j] == '*':  # 불의 위치
        q1.append([i,j])
        visited1[i][j] = 0
      elif board[i][j] == '@':  # 상근이의 시작 위치
        q2.append([i,j])
        visited2[i][j] = 0

  while q1:   # 불의 방문 시간을 구한다. (BFS)
    item = q1.popleft()
    x = item[0]; y = item[1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 범위를 벗어나면 pass
        continue
      if board[nx][ny] == '#' or visited1[nx][ny] >= 0: # 벽이거나 방문한 노드이면 pass
        continue
      visited1[nx][ny] = visited1[x][y] + 1
      q1.append([nx,ny])
  
  while q2:
    item = q2.popleft()
    x = item[0]; y = item[1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 범위를 벗어나면 상근이가 탈출했다는 뜻.
        print(visited2[x][y] + 1)
        return
      if board[nx][ny] == '#' or visited2[nx][ny] >= 0:
        continue
      if visited1[nx][ny] <= visited2[x][y] + 1 and visited1[nx][ny] != -1:
        continue
      visited2[nx][ny] = visited2[x][y] + 1
      q2.append([nx,ny])

  print('IMPOSSIBLE')

T = int(input())
for _ in range(T):
  fire()
