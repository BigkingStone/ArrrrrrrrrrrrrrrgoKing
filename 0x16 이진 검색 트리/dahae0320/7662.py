from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
for t in range(int(input())):
  min_heap = []
  max_heap = []
  dic = defaultdict(int)
  for k in range(int(input())):
    op, num = input().strip().split()
    num = int(num)
    if op == "I":
      heappush(min_heap, num)
      heappush(max_heap, -num)
      dic[num] += 1
    elif op == "D" and num == -1:
      while min_heap:
        val = heappop(min_heap)
        if dic[val] == 0: continue
        dic[val] -= 1
        break
    elif op == "D" and num == 1:
      while max_heap:
        val = -heappop(max_heap)
        if dic[val] == 0: continue
        dic[val] -= 1
        break
  ans = []
  if sum(dic.values()) != 0:
    while max_heap:
        val = -heappop(max_heap)
        if dic[val] == 0: continue
        ans.append(val)
        break
    while min_heap:
        val = heappop(min_heap)
        if dic[val] == 0: continue
        ans.append(val)
        break
    print(" ".join(map(str, ans)))
  else:
    print("EMPTY")
