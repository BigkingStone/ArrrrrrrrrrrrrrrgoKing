import sys
input = sys.stdin.readline
heap = [2**31 for _ in range(100001)]
sz = 0

def push(x):
  global sz
  sz += 1
  heap[sz] = x
  cur = sz
  while cur != 1:
    if heap[cur] <= heap[cur//2]: break
    heap[cur], heap[cur//2] = heap[cur//2], heap[cur]
    cur = cur // 2

def top():
  return heap[1]

def pop():
  global sz
  heap[1] = heap[sz]
  sz -= 1
  cur = 1
  while 2*cur <= sz:
    lc= 2*cur; rc = 2*cur+1
    maxChild = lc
    if rc <= sz and heap[lc] < heap[rc]:
      maxChild = rc
    if heap[cur] >= heap[maxChild]: break
    heap[cur], heap[maxChild] = heap[maxChild], heap[cur]
    cur = maxChild

n = int(input())
for _ in range(n):
  x = int(input())
  if x == 0:
    if sz == 0: print(0)
    else: 
      print(top())
      pop()
  else:
    push(x)
