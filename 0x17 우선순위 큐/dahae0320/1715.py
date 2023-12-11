from heapq import heapify, heappush, heappop
n = int(input())
heap = [int(input()) for _ in range(n)]
heapify(heap)
ans = 0
while len(heap) > 1:
  a = heappop(heap)
  b = heappop(heap)
  ans += a+b
  heappush(heap, a+b)
print(ans)
