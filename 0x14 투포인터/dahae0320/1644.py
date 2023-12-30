import sys
input = sys.stdin.readline
n = int(input())
# 소수 구하기
isPrime = [True for _ in range(n+1)]
for i in range(2, n+1):
  if not isPrime[i]: continue
  for j in range(i*i, n+1, i):
    isPrime[j] = False
prime = [i for i in range(2, n+1) if isPrime[i]]
# 투 포인터로 연속합 계산하기
m = len(prime)
en = 0
tot = prime[0] if prime else 0
cnt = 0
for st in range(m):
  while en+1 < m and tot < n:
    en += 1
    tot += prime[en]
  if en == m: break
  if tot == n: cnt += 1
  tot -= prime[st]
print(cnt)
