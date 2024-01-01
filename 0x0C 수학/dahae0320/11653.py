import sys
input = sys.stdin.readline
n = int(input())
for i in range(2, n+1):
  while n % i == 0:
    print(i)
    n = n // i

# 더 빠른 방법(최적화)
import sys
input = sys.stdin.readline
n = int(input())
for i in range(2, int(n**0.5)+1):
  while n % i == 0:
    print(i)
    n = n // i
if n != 1: print(n)
