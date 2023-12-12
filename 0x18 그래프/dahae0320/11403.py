from collections import deque
import sys
input = sys.stdin.readline

# 1. 인접 리스트에 그래프 표기하기
n = int(input())
adj = [[] for _ in range(n+1)]
ans = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
  arr = list(map(int, input().strip().split()))
  for j in range(n):
    if arr[j] == 1:  adj[i].append(j+1)

# 2. 모든 정점을 기준으로 한번씩 BFS 돌기
for i in range(1,n+1):
  vis = [False for _ in range(n+1)]
  q = deque([i])
  vis[i] = True
  while q:
    cur = q.popleft()
    for nxt in adj[cur]:
      if vis[nxt] and nxt != i: continue
      q.append(nxt)
      vis[nxt] = True
      ans[i][nxt] = 1

# 3, 출력
for i in range(1, n+1):
  print(" ".join(map(str, ans[i][1:])))
