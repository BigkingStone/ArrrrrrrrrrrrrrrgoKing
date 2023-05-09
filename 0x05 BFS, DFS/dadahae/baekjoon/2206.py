from collections import deque
N, M = map(int, input().split())
matrix = [ [int(i) for i in input()] for _ in range(N) ]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()
# visited[x][y][0]: (x,y)까지 올 때 벽을 부수지 않고 걸린 거리
# visited[x][y][1]: (x,y)까지 올 때 벽을 한 번이라도 부수고 걸린 거리, (x,y)도 부수는 벽에 포함
visited = [[[0,0] for _ in range(M) ] for _ in range(N)] 
minDist = -1

# BFS
q.append([0,0,0])
visited[0][0][0] = visited[0][0][1] = 1   # 첫 시작은 벽안뚫, 벽뚫 둘 다 스타트를 끊어준다.
while q:
  x, y, broken = q.popleft()
  if x == (N-1) and y == (M-1):   # 먼저 (N,M)에 도착하면 가장 최단 거리이므로 계산은 끝이 난다.
    minDist = visited[x][y][broken]
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= N or ny >= M or nx < 0 or ny < 0: continue
    # (x,y) 자리의 벽을 부수지 않고 갈 수 있을 때
    if (matrix[nx][ny] == 0) and (visited[nx][ny][broken] == 0):
      q.append([nx,ny,broken])
      visited[nx][ny][broken] = visited[x][y][broken] + 1
    # (x,y) 자리의 벽을 부술 수 있을 때
    if (broken == 0) and (matrix[nx][ny] == 1) and (visited[nx][ny][1] == 0):
      q.append([nx,ny,1])
      visited[nx][ny][1] = visited[x][y][broken] + 1

print(minDist) 
