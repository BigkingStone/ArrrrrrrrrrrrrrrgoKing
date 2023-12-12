from collections import deque
import sys
input = sys.stdin.readline
n = int(input())  # 동기의 수
m = int(input())  # 리스트의 길이
adj = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
for i in range(m):
  u, v = list(map(int, input().strip().split()))
  adj[u].append(v)
  adj[v].append(u)
q = deque()
if adj[1]:  
  q.append(1)
  dist[1] = 0
ans = 0
while q:
  cur = q.popleft()
  for nxt in adj[cur]:
    if dist[nxt] != -1: continue
    if dist[cur] >= 2: continue
    q.append(nxt)
    dist[nxt] = dist[cur] + 1
    ans += 1
print(ans)
