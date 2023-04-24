import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque( range(1,N+1) )
new_queue = deque()

while len(queue) != 0:
  for _ in range(K-1):  # K-1번까지 반복
    queue.append( queue.popleft() )
  new_queue.append( str(queue.popleft()) ) # K번째 요소는 새로운 큐에 추가

print('<' + ', '.join(new_queue) + '>')
