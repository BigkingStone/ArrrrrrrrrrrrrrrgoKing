```python
#######그림########
#도화지에 1로 연결된 그림의 개수, 그림들 중 가장 큰 그림
#그림이 하나도 없는 경우 그림의 넓이는 0 -> 기본 0을 넣고 시작
#bfs로 그림의 시작점에 따라 하나씩 방문하면 그림의 크기를 구한다(pop할때 마다 그림의 크기 1증가
#방문 표시로는 0으로 한다. 다시 들어가더라도 없는 그림처럼
#한 그림이 마무리 되면 다른 1을 찾아서 시작 -> 그림 개수 +1(그림의 크기 저장할 list append(그림 크기))
#입력할 도화지 2차원 list, BFS 큐, 그림의 크기 저장할 list 
from sys import stdin
from collections import deque
input = stdin.readline
N,M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
size_draws = []
draw = deque()
#북동남서
dx = [1,0,-1,0]
dy = [0,1,0,-1]
#도화지 탐색 2차원이므로 2중 forloop로 확인
for i in range(N):
    for j in range(M):
        #시작 그림 지점을 찾자
        if paper[i][j] == 0:
            continue
        else:
            draw.append((i,j))
            paper[i][j] = 0
            #draw가 empty 될때 까지
            size = 0
            #queue가 비어져 있다면 while을 멈춘다 한 그림의 탐색이 마친것
            while draw:
                for k in range(4):
                    cur_dx = dx[k] + draw[0][0]
                    cur_dy = dy[k] + draw[0][1]
                    #범위를 초과,,
                    if cur_dx >= N or cur_dy >= M or cur_dx < 0 or cur_dy < 0:
                        continue
                    elif paper[cur_dx][cur_dy] == 1:
                        draw.append((cur_dx,cur_dy))
                        paper[cur_dx][cur_dy] = 0
                    else: # == 0이라면
                        continue
                #위 과정을 거치고 pop을 한다. 
                draw.popleft()
                size += 1 #pop 할때마다 size증가
            #size 추가
            size_draws.append(size)
print(len(size_draws))
if size_draws:
    print(max(size_draws))
else:
    print(0)
```
