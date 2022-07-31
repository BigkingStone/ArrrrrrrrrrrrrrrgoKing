#하노이 탑 문
#n-1개를 옮길수 있다면 n개도 옮길수 있다.. 
#귀납적 사고를 통해서 풀 수 있다.
#입력: 원판의 개수
#출력: 옮긴횟수, 수행순서
import sys

def hanoi(n, a, b):
    if n == 1: 
        print(a, b)
        return
    hanoi(n-1, a, 6-a-b)
    print(a, b)
    hanoi(n-1, 6-a-b, b)
    

n = int(input())
print(2**n - 1)
hanoi(n,1,3)
