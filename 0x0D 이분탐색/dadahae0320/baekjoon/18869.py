from bisect import bisect, bisect_left, bisect_right
import sys
input = sys.stdin.readline
m, n = list(map(int, input().strip().split()))

# (1) 각 우주에 있는 행성 크기 순서 매기기 - 좌표 압축
arr = []
for _ in range(m):
  arr.append(list(map(int, input().strip().split())))
uni = [[] for _ in range(m)]  # arr에서 정렬, 중복이 제거된 값이 들어간다.
for i in range(m):
  tmp = sorted(arr[i])  # arr[i]을 좌표 압축 하기 전에 정렬해준다.
  for j in range(n):
    if j == 0 or tmp[j] != tmp[j-1]:  # 유일한 값 tmp[j]를 uni[i]에 추가한다.
      uni[i].append(tmp[j])
cor = [[] for _ in range(m)]  # arr의 좌표 압축이 들어간다.
for i in range(m):
  for j in range(n):
    target = arr[i][j]
    idx = bisect(uni[i], target)
    cor[i].append(idx)

# (2) 쌍 찾기 - 좌표 압축
uni2 = []
cor.sort()
for i in range(m):
  if i == 0 or cor[i] != cor[i-1]:
    uni2.append(cor[i])
ans = 0
for u in uni2:
  lidx = bisect_left(cor, u)
  ridx = bisect_right(cor, u)
  k = ridx - lidx
  if k == 1: continue
  ans += k*(k-1)//2
print(ans)
