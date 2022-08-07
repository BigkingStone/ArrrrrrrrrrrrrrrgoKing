def func(cur, tot):
    global cnt
    if cur == n:
        if tot == s: cnt += 1 
        return
    func(cur + 1, tot)
    func(cur + 1, tot + arr[cur])
            
import sys
input = sys.stdin.readline
n,s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
cnt = 0

func(0, 0)
if s == 0:
    cnt -= 1
print(cnt)
