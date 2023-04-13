####나이트 이동####
# 체스판에 나이트가 이동하려는 칸이 주어진다면 그 칸을 몇번만에 갈 수 있을까?
# 움직이는 방향,,총 8방향으로 움직일 수 있다.
# 북: (x+1,y+2),(x-1,y+2), 동: (x+2, y+1),(x+2, y-1), 남: (x+1,y-2), (x-1,y-2) 서: (x-2, y-1), (x-2, y+1)
# 판 (4<=ㅣ<=300)
#입력: 테스트케이스, {판, 현재 위치, 목적 위치}
#출력: 각케이스별 걸리는 시간

import sys
from collections import deque
input = sys.stdin.readline
#입력받아야할 데이타
T = int(input())
N, M = 0,0#체스판 크기(순회시 범위)
fp_x,fp_y=0,0#firstpoint x,y
tp_x,tp_y=0,0#targetpoint x,y
#이동 백터
# 북: (x+1,y+2),(x-1,y+2), 동: (x+2, y+1),(x+2, y-1), 남: (x+1,y-2), (x-1,y-2) 서: (x-2, y-1), (x-2, y+1)
dx = [1,-1 ,2,2 ,1,-1 ,-2,-2]
dy = [2,2 ,1,-1 ,-2,-2 ,-1,1]
#결과값 저장
result = []
#케이스 확인
for i in range(T):
    #queue
    night = deque()
    #체스판 초기화
    cheses = [[-1]*300 for _ in range(300)]
    cheses_size = int(input())
    N,M = cheses_size, cheses_size
    fp_x,fp_y = map(int, input().split())
    tp_x,tp_y = map(int, input().split())
    cheses[fp_x][fp_y] = 0
    night.append((fp_x,fp_y))
    end =0

    while night:
        x,y = night.popleft()
        #이동전 바로 시작과 타겟이 같다면,, 바로 종료
        if x == tp_x and y == tp_y:
            result.append(cheses[x][y])
            break
        for j in range(len(dx)):
            #2차원 모든 이동방향으로 확인
            nx = x + dx[j]
            ny = y + dy[j]
            #범위 안에 있다
            if 0<= nx < N and 0<= ny < M:
                #target지점에 도착하면 값 저장후 break
                if nx == tp_x and ny == tp_y:
                    cheses[nx][ny] = cheses[x][y] + 1
                    result.append(cheses[nx][ny])
                    end = 1
                # < 0 즉 방문하지 않은 곳이라면 체스판에 방문표시(+1) 그리고  append
                if cheses[nx][ny] < 0:
                    cheses[nx][ny] = cheses[x][y] + 1
                    night.append((nx,ny))
            #범위 밖이면 continue
            else:
                continue
        #end == 1이라면 이 test 종료 -> while 문 나감
        if end == 1:
            break

for i in range(len(result)):
    print(result[i])
