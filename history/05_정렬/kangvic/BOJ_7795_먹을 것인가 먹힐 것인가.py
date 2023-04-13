import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    cnt = 0 # 쌍의 개수
    N,M = map(int, input().split()) # 5 3
    arr = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(N):
        arr.append([a[i],0])
    for i in range(M):
        arr.append([b[i],1])
    arr.sort()
    ans = 0
    cnt = 0
    for i in range(N+M):
        if arr[i][1] == 0: # A라면 cnt를 ans에 더함
            ans += cnt
        else:
            cnt += 1 # B라면 cnt += 1
    print(ans)
