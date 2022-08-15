import sys
input = sys.stdin.readline
n,c= map(int, input().split())

arr = list(map(int, input().split())) # 1 1 100 50 100 100 50
valList = []
#안의 val값 나온 순서대로 set처럼 넣어놓자 # 1 100 50
j = 0 
for i in range(n):
    if arr[i] in valList:
        continue
    valList.append(arr[i])
    j+=1 


#valList의 count를 넣자,, count함수사용 # 2 3 2
cntList = [0]* len(valList)
for i in range(len(cntList)):
    cntList[i] = arr.count(valList[i])

#출력
while sum(cntList) != 0:
    maxCnt = max(cntList) # 3 # 2 # 2
    maxValIndx = cntList.index(maxCnt) # 1 # 0 # 2
    for i in range(maxCnt):
        print(valList[maxValIndx], end = ' ') # 100 100 100 # 1 1 # 50 50
    cntList[maxValIndx] = 0 # 2 0 2 # 0 0 2 # 0 0 0
