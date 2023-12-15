import sys
input = sys.stdin.readline
n = int(input())
d = [0] + list(map(int, input().strip().split())) # 초기 카드팩 가격, # 카드를 i개 구매할 때 지불하는 최대 값
for i in range(2, n+1):
  for j in range(1, i):
    d[i] = max(d[i-j]+d[j], d[i])
print(d[n])
