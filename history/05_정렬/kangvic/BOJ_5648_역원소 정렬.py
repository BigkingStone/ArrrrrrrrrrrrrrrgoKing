#입력
#입력을 무작위로,, 띄어쓰기 엔터 상관없이 입력을 받는데,, 어떻게 할까?
#while로 배열의 길이가 n이 된다면 stop
import sys
input = sys.stdin.readline
n = 10**6
arr = []
while len(arr) <= n:
    inputStr = input().rstrip().split()
    for i in range(len(inputStr)):
        arr.append(inputStr[i])
    n = int(arr[0])
del arr[0]
#원소 거꾸로 하기
#입력을 한줄 받고나서 바로 
#for i in range(len(arr)):
#    for j in range(len(arr[i])//2):
        # 앞뒤를 바꾼다.
        # 바꾼후 모두 int로 치환해서 0은 알아서 없어진다.
for i in range(n):
    arr[i] = arr[i][::-1]
    arr[i] = int(arr[i])
#sort후 출력
arr.sort()
for i in range(n):
    print(arr[i])
