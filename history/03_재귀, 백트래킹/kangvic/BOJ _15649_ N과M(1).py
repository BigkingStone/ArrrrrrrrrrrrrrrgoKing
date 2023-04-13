#####N,M
#1<=N,M<=8
N,M = map(int,input().split())
arr = [0]*10
issues = [False]*10

def func(k):
    if k == M : #M개를 모두 다 선택했다면 멈춰,,
        for i in range(M):
            print(arr[i],end = ' ')
        print()
        return 
    for i in range(1,N+1):
        if issues[i] == False: #아직 i를 사용 하지 않았더라면,,실행
            arr[k] = i# k일때 i를 대입
            issues[i] = True #i
            func(k+1) #다음번째 칸을 확인
            issues[i] = False # 다시 왔으면 i를 사용하지 않은것으로 초기화
func(0)
