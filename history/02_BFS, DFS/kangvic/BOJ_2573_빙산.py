######빙산#################################################################
#빙산의 각 부분별 높이정보가 숫자로 2차원 배열상 존재
#빙산이 아닌 부분은 바다로 0으로 채워짐
# 빙산은 매년 주위(동서남북)에 바다에 접한 면의 수의 따라 그만큼 높이가 작아진다.
    # 예시  000 -> 000
    #      042    021  
# 빙산의 한 덩어리가 두 덩어리 이상으로 분리되는 시간을 출력!
#문제
# 두 덩어리로 떨어져 있는 것을 확인하는 방법..
    #동서남북으로 떨어져있다..붙어있는것만,, queue에 들어가니깐,, 그 queue의 개수가 2개 이상이면 멈추자
    # for문으로 빙하의 시작지점을 기준으로 계속 한다.. 
# 빙산들의 높이를 어떤것을 기준으로 먼저 확인하고 방문 표시를 할까,,
    #빙산 queue에 사방으로 순회하면서 처음 방문후 주변의 바다 유무를 확인하며 바다맵안 방문부분의빙산높이를 줄인다.
# 반복을 어떻게 하면 종료하게 할까,,
    # 빙산이 모두 0,,
        #sum(바다) < 1일때 종료
    # 빙산 두덩이이상으로 떨어진다면,,  
        #queue의 개수가 2개 이상이면,, 멈추자!! 
            #즉 하나의 시작 지점으로 해서 bfs가 한번 끝나고 또 만약 시작 지점이 존재하다면,, 멈춰!!
#필요자료구조   
    #빙산 큐(매년 초기화), 첫해방문list, 매년방문list(매년 초기화), 바다맵2차원배열 + 바다맵 크기N*M, 사방벡터

from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int,input().split())
marin = [list(map(int, input().split())) for _ in range(N)]
ice_queue = deque()

dx = [-1,0,1,0]
dy = [0, 1, 0, -1]
year = 0

while sum(sum(marin, [])) != 0: # 빙산탐방중 한 queue를 마치고 나머지를 탐방중 방문하지 않은 곳에 0이상인 빙산이 있는 경우 year를 출력후 멈춘다// 모든 빙산이 0이 된다면 0을 출력후 멈춘다.
    visited = [ [False] * M for _ in range(N)]#한번 모든 바다를 탐방후 reset이 필요하다.
    year += 1#빙하 탐방 시작 시 +1
    numOfQueue = False #빙하 탐방을 했는지 확인하는 flag
    #빙산을 탐방한다.이중 for
    for i in range(N):
        for j in range(M):
            if marin[i][j] == 0:
                continue
            else:#0보다 클때,,
                if visited[i][j] == True: #이미 방문한 곳이라면,, continue
                    continue
                if numOfQueue == True: #0보다 큰 빙하가 있고, 이곳은 방문한 곳이 아니고, 이미 한번 빙하탐방을 한번 마쳤다면 이는 다른 빙하이다.
                        print(year-1)#한번 탐방을 하고 나가야 그 해에 두덩이로 나누어 진것을 알 수 있다.
                        sys.exit(0)
                ice_queue.append((i,j))
                visited[i][j] = True
                while ice_queue:
                    #빙하를 탐방했다는 표시!!
                    numOfQueue = True
                    x,y = ice_queue.popleft()
                    #빙하 4방으로 바다인접, 빙하인접확인
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx >= N or nx < 0 or ny >= M or ny < 0:
                            continue
                        if visited[nx][ny] == True: continue
                        if marin[nx][ny] == 0: #바다 인접이고 0이 아니라면 -1
                            if marin[x][y] == 0:
                                continue
                            marin[x][y] -= 1
                        elif marin[nx][ny] >0:#위에서 방문확인 했으니,, 여기서는 그냥 append만 해주면 된다.
                            ice_queue.append((nx,ny))
                            visited[nx][ny] = True
print(0)
