import sys
input = sys.stdin.readline
n = int(input())
heap = [2**31 for _ in range(100001)]
sz = 0

def push(x):
  global sz
  sz += 1
  heap[sz] = x
  cur = sz
  while cur // 2 > 0:
    if heap[cur] >= heap[cur//2]: break
    heap[cur], heap[cur//2] = heap[cur//2], heap[cur]
    cur = cur // 2
	/*
	while cur != 1:
    if heap[cur] >= heap[cur//2]: break
    heap[cur], heap[cur//2] = heap[cur//2], heap[cur]
    cur = cur // 2
  */


def top():
  return heap[1]

def pop():
  global sz
  heap[1] = heap[sz]
  sz -= 1
  cur = 1
  while 2*cur <= sz:
    lc = 2*cur; rc = 2*cur+1
    mc = lc # 두 자식 중 가장 작은 자식의 인덱스를 담을 예정
    if rc <= sz and heap[lc] > heap[rc]:
      mc = rc
    if heap[cur] <= heap[mc]: break
    heap[cur], heap[mc] = heap[mc], heap[cur]
    cur = mc

for _ in range(n):
  x = int(input())
  if x == 0:
    # top, print
    if sz == 0: print(0)
    else:
      print(top())
      pop() # pop
  else:
    # push
    push(x)
