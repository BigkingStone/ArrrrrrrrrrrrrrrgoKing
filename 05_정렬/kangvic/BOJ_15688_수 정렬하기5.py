#counting sort
isnum = [0]*2000001
HALF = len(isnum)//2
n = int(input())
for i in range(n):
    t = int(input())
    isnum[t+HALF] += 1
for i in range(len(isnum)):
    while isnum[i] > 0:
        print(i-HALF)# 음수도 이렇게 거를수 있다.
        isnum[i] -= 1
