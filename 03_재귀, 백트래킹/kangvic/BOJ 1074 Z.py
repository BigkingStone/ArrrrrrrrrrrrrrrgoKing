#ㅋ#
#입력: n , r, c
#출력: r,c에 도착한 순서 출력,,
#4등분한것은 이전에 앞에서 한 부분을 중복,, 각 등분
# r,c가 위치한 곳 (1,2,3,4)에 따라 달라,, -> 1: f(n-1,r,c) 2: h*h + f(n-1,r,c), 3: 2*h*h +,,
#   h = 2**(n-1)
#base condition으로 n==0이면 return 0
import sys
input = sys.stdin.readline

def Z(n: int, r: int, c: int):
    if n == 0: return 0
    h = 2**(n-1)
    if r < h and c < h: return Z(n-1,r,c)
    if r < h and c >= h: return h*h + Z(n-1,r,c - h)
    if r >= h and c < h: return 2*h*h + Z(n-1,r - h,c)
    return 3*h*h + Z(n-1,r-h,c-h)

n,r,c = map(int, input().rstrip().split())
print( Z(n,r,c) )
