N, M = map(int, input().split())
arr = [0 for _ in range(M)] # M자리 배열
isused = [False for _ in range(N+1)]  # 1~N까지의 수가 사용된 적 있는지 확인하는 배열

def nm(k): # arr의 자리수 k, M자리 배열을 채워주는 함수
  if k == M:
    print(" ".join(map(str, arr)))
    return 
  for i in range(1,N+1):  # 1부터 N까지 
    if not isused[i]: # 사용된 수가 있는지 확인
      arr[k] = i
      isused[i] = True
      nm(k+1)
      isused[i] = False

nm(0)
