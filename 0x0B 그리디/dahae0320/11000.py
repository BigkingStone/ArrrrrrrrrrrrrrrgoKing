import sys
input = sys.stdin.readline
n = int(input())
event = []
for _ in range(n):
  s, f = list(map(int, input().strip().split()))
  event.append([s, 1])
  event.append([f, -1])
event.sort()
idx = 0 # 현재 이벤트의 번호
cur = 0 # curtime에서 열릴 수 있는 강의실 개수
curtime = event[0][0] # 현재 시간
ans = 0 # 가장 많이 열리는 강의실 개수
while True:
  while idx < n*2 and curtime == event[idx][0]:
    cur += event[idx][1]
    idx += 1
  ans = max(ans, cur)
  if idx >= n*2: break
  curtime = event[idx][0]
print(ans)
