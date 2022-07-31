from collections import deque

def bfs(x,y):
    #bfs로 방문한 노드를 큐에 저장(x,y)
    queue = deque()
    queue.append((x,y))
    while queue:
        #큐에서 하나 꺼낸다
        x,y = queue.popleft()
        #현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로의 범위를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽에 위치한 경우 무시
            if miro[nx][ny] == 0:
                continue
            #처음 방문한 경우
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1 #직전노드에 거리 1을 더해가며 처음 시작노드와의 거리를 기록해 나간다.
                queue.append((nx,ny))
                #ex)0 1 2
                #   1 2 3
                #   2 3 4 대충 이런 느낌으로 간다는 것이다.
                
    return miro[n-1][m-1]#최종 끝에 저장된 거리를 반환한다.
    
n,m = map(int,input().split())
miro = [list(map(int, input())) for _ in range(n)]
#이동할 방향 정의(좌,우,하,상)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bfs(0,0))
