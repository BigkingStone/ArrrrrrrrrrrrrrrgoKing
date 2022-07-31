import sys
from collections import deque
input = sys.stdin.readline
#입력
R,C = map(int , input().split())#R,C
#미로 -> 지훈, 미로 -> 불 MAX -> 1000*1000
miroj = [[-1]*C for _ in range(R)]
mirof = [[-1]*C for _ in range(R)]


#지훈, 불 queue 생성
queuej = deque() 
queuef = deque()

    #미로 입력
for i in range(R):
    str = input().rstrip()
    for j in range(C):
        miroj[i][j] = str[j]
        mirof[i][j] = str[j]
        #미로 벽:5, 통로:0, 지훈or불 : 0 -> typeerror때문에,, 모두 정수로 바꾸고 연산을 하자
        if miroj[i][j] == '#':
            miroj[i][j] = -5
            mirof[i][j] = -5
        elif miroj[i][j] == '.':
            miroj[i][j] = -1
            mirof[i][j] = -1
        elif miroj[i][j] == "J":#J위치를 queuej에 넣는다,
            miroj[i][j] = 0
            mirof[i][j] = -1
            queuej.append((i,j))
        elif mirof[i][j] == 'F':#F위치를 queuef에 넣는다.
            miroj[i][j] = -1
            mirof[i][j] = 0
            queuef.append((i,j))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
#불 미로 이동 BFS
while queuef:
    x,y = queuef.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<R and 0<=ny<C:
            if mirof[nx][ny] != -5 and mirof[nx][ny] < 0:
                queuef.append((nx,ny))
                mirof[nx][ny] = mirof[x][y] + 1
        else:
            continue


#지훈 미로 이동 BFS
while queuej:
    x,y = queuej.popleft()
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx >= R or nx < 0 or ny >= C or ny < 0:#큐에는 크기순으로 들어가므로 최초 출력시 가능
            print(miroj[x][y]+1)
            sys.exit(0)
        if miroj[nx][ny] == -5 or miroj[nx][ny] > 0:#벽이거나 방문한 곳
            continue
        if miroj[x][y] + 1 < mirof[nx][ny] or mirof[nx][ny] == -1:#불보다 미리 왔다면
            queuej.append((nx,ny))
            miroj[nx][ny] = miroj[x][y] + 1

print("IMPOSSIBLE")
