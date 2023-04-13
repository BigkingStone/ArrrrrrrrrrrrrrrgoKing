def func(k):
    global cnt
    if k == N:
        cnt += 1
        return
    for i in range(N):
        if issued_y[i] or issued_lxy[i+k] or issued_rxy[k-i + N-1]:
            continue
        issued_y[i] = True
        issued_lxy[i+k] = True
        issued_rxy[k-i + N-1] = True
        func(k+1)
        issued_y[i] = False
        issued_lxy[i+k] = False
        issued_rxy[k-i + N-1] = False

import sys
input = sys.stdin.readline
N = int(input())
issued_y = [False]*40
issued_rxy = [False] * 40
issued_lxy = [False] * 40
cnt = 0
func(0)
print(cnt)
