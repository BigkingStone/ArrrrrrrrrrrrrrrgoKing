#카드
n = int(input())
arr = []
cnt = [0]*n
for i in range(n):
    arr.append(int(input()))
arr.sort()
cnt = 0 # 현재 나온 수들의 횟수
j = 0 # 가장 많이 나온 횟수
max_cnt = 2**62 + 1 # 가장많이 나온 횟수의 숫자,,(가장 작은 값)
for i in range(0,n):
    if i == n-1:
        if arr[i-1] == arr[i]:
            cnt += 1
        if j < cnt:
            j = cnt
            max_cnt = arr[i-1]
        elif j == cnt:
            if max_cnt > arr[i-1]:
                max_cnt = arr[i-1]
        break
     #i가 n-1일때,, 그냥 continue하고 끝나버린다. 위의 경우를 확인해주어야 한다.

    if arr[i-1] == arr[i] or i == 0: #이전 값과 같으면 횟수 증가
        cnt += 1 
        continue
    if j < cnt: #달라지면 이제 J, max_cnt를 업데이트 해준다.. 조건에 맞게
        j = cnt
        max_cnt = arr[i-1]
    elif j == cnt:
        if max_cnt > arr[i-1]:
            max_cnt = arr[i-1]
    cnt = 1# 다시 초기화 하고 현재값을 넣어준것,
print(max_cnt)
