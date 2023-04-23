# Deque(stack)을 이용한 풀이
# 시간을 단축하기 위해 표준입출력을 사용하였다.
import sys
from collections import deque
input = sys.stdin.readline

stk1 = deque(input().rstrip())
stk2 = deque()
M = int(input())

for i in range(M):
  inst = list(input().split())
  
  if inst[0] == 'L':
    if len(stk1) != 0:
      stk2.append( stk1.pop() )
  
  elif inst[0] == 'D':
    if len(stk2) != 0:
      stk1.append( stk2.pop() )
  
  elif inst[0] == 'B':
    if len(stk1) != 0:
      stk1.pop()

  elif inst[0] == 'P':
    stk1.append( inst[1] )

sys.stdout.write( ''.join(stk1) + ''.join(reversed(stk2)) )
