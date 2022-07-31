import sys
from collections import deque
input = sys.stdin.readline
space = [-1]*100001#1차원 위치(0~100000)
N,K = map(int,input().split())
queue = deque([N])
space[N] = 0
#이동
dx = [-1,1,2]#2는 나중에 배수로 처리 할것
while space[K] == -1:
    x = queue.popleft()
    for i in [x-1,x+1,x*2]:
        if i > 100000 or i < 0:
            continue
        if space[i] > 0:#이미 방문한 곳이라면,
            continue    
        space[i] = space[x]+1
        queue.append(i)

print(space[K])
