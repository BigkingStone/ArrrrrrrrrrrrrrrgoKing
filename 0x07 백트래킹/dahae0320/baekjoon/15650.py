N, M = map(int, input().split())
arr = [0 for _ in range(M)] # M자리 배열 (0-indexed)
isused = [False for _ in range(N+1)]  # 1~N까지의 수가 쓰인 적 있는지 확인하는 배열

def nm(k):  # n과 m을 만족하는 수열을 출력하는 함수
  if k == M:  # k값이 M과 같으면 배열을 다 채웠으므로 출력 (k는 인덱스 역할)
    print(" ".join(map(str, arr)))
    return 
  idx = arr[k-1]+1 if k != 0 else 1
  for i in range(idx, N+1):
    if not isused[i]:
      arr[k] = i
      isused[i] = True
      nm(k+1)
      isused[i] = False

nm(0)
