from collections import deque

def BFS(L, R, C, st, building):
  visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
  visited[st[0]][st[1]][st[2]] += 1
  dx = [0,0,-1,1,0,0]
  dy = [-1,1,0,0,0,0]
  dz = [0,0,0,0,-1,1]
  q = deque([st])
  while q:
    z, y, x = map(int, q.popleft())
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if nx >= C or nx < 0 or ny >= R or ny < 0 or nz >= L or nz < 0: # 빌딩 영역을 벗어날 때
        continue
      if building[nz][ny][nx] == "#": # 막힌 곳일 때
        continue
      if visited[nz][ny][nx] >= 0: # 방문한 적이 있을 때
        continue
      if building[nz][ny][nx] == "E": # 탈출 할 수 있는 곳일 때, 탈출하고 구문 종료
        print("Escaped in " + str(visited[z][y][x]+1) + " minute(s).")
        return 
      visited[nz][ny][nx] = visited[z][y][x] + 1
      q.append([nz,ny,nx])
  print("Trapped!")


while True:
  L,R,C = map(int, input().split())
  if L == 0 and R == 0 and C == 0:
    break
  building = [[0 for _ in range(R)] for _ in range(L)]
  st = []
  for z in range(L):
    for y in range(R):
      building[z][y] = list(map(str, input()))
      for x in range(C):
        if building[z][y][x] == "S":
          st = [z,y,x]
    input()
  
  BFS(L, R, C, st, building)
