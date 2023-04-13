from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [-1]*(F+1)
cnt = 0

q = deque([S])
visited[S] += 1
while q:
  floor = q.popleft()
  if floor == G:  # 현재 층수가 G층이면 BFS 탐색 종료
    print(visited[floor])
    quit()
  for move in [U,-D]: # 현재 층수에서 갈 수 있는 층수를 구한다. (현재층+U층 혹은 현재층-D층)
    next = floor + move
    if next > F or next < 1:  # 건물 층수의 범위를 벗어나면 제외
      continue
    if visited[next] > -1: # 이미 방문한 층수면 제외
      continue
    visited[next] = visited[floor] + 1
    q.append(next)

print("use the stairs")
