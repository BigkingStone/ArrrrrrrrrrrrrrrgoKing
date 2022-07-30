from collections import deque

N, M = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
maze = []
visited = []
for n in range(N):
  line = input()
  maze.append( [int(line[i]) for i in range(M)] )
  visited.append( [False]*M )

q = deque([[0,0]])
while q:
  item = q.popleft(); x = item[0]; y = item[1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if maze[nx][ny] == 0 or visited[nx][ny] == True:
      continue
    maze[nx][ny] = maze[x][y] + 1
    visited[nx][ny] = True
    q.append([nx,ny])

print(maze[N-1][M-1])
