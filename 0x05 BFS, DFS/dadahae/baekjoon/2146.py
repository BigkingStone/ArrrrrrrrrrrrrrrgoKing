from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = [[] for _ in range(n)]
for i in range(n):
  board[i] = list(map(int, input().strip().split()))
island = [[-1 for _ in range(n)] for _ in range(n)]
num = 0
edges = []  
# 1. 섬의 총 개수 구하기 (시작점이 여러개인 BFS)
for i in range(n):
  for j in range(n):
    if board[i][j] == 0 or island[i][j] != -1: continue
    edge = []
    q = deque([[i,j]])
    island[i][j] = num
    edge.append([i, j])
    while q:
      x, y = q.popleft()
      for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue # 범위를 벗어나면
        if board[nx][ny] == 0: continue # 섬이 아니면
        if island[nx][ny] != -1: continue # 방문한 적이 있으면
        island[nx][ny] = num
        edge.append([nx, ny]) # num번 섬의 땅이 들어간다.
        q.append([nx, ny])
    edges.append(edge)  # 2. num범 섬의 땅을 기록한다. (가장자리 값만 알면 되지만, 모든 땅을 넣어도 계산에는 문제없다.)
    num += 1
# 3. 모든 섬에 대해서 1,2번을 진행하고 섬과 섬간의 가장 짧은 거리를 구한다.
mi = 100001
for i in range(num):
  ans = 100001
  dist = [[-1 for _ in range(n)] for _ in range(n)]
  q = deque(edges[i])
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx = dx[k] + x
      ny = dy[k] + y
      if nx < 0 or ny < 0 or nx >= n or ny >= n: continue # 범위를 벗어나면
      if island[nx][ny] == i: continue  # 현재 섬이라면
      if island[nx][ny] != i and island[nx][ny] != -1: # 다른 섬이면
        ans = dist[x][y] + 1
        break
      if dist[nx][ny] != -1: continue # 방문한 적이 있으면
      dist[nx][ny] = dist[x][y] + 1
      q.append([nx, ny])
    mi = min(ans, mi)
print(mi)
