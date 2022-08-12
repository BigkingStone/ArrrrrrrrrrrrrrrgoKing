from collections import deque

def BFS(x,y, k):
  q = deque([[x,y]])
  visited[x][y] = True
  while q:
    x, y = map(int, q.popleft())
    for i in range(4):  # 상하좌우로 인접한 지역을 탐색한다.
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if visited[nx][ny]: # 이미 방문한 지역이면 탐색하지 않는다.
        continue
      if board[nx][ny] <= k:  # 물의 높이(k)보다 작거나 같으면 잠긴다.
        continue
      visited[nx][ny] = True
      q.append([nx,ny])

N = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = []
board = []
for i in range(N):
  board.append( list(map(int, input().split())) )

max_cnt = 0
for k in range(0, 100):  # 물의 높이(k)를 0부터 99까지 모두 확인해본다. (물에 젖지 않는 경우도 있다)
  cnt = 0
  visited = [[False for _ in range(N)] for _ in range(N)]
  for i in range(N):  # board를 처음부터 순회한다.
    for j in range(N):
      if visited[i][j] == False and board[i][j] > k:  # 방문하지 않고 물높이(k)보다 높은 지역을 시작노드로 삼는다.
        BFS(i,j, k)
        cnt += 1  # BFS로 방문을 끝내면 잠기지 않는 지역의 개수를 +1 해준다.
  if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)
