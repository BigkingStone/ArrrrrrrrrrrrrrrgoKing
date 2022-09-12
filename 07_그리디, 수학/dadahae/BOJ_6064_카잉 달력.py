def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a, a)

def lcm(a,b):
  return a // gcd(a,b) * b

def solve(m,n,x,y):
  if x == m: x = 0
  if y == n: y = 0
  l = lcm(m,n)
  for i in range(x, l+1, m):
    if i == 0: continue
    if i % n == y:
      return i
  return -1

T = int(input())
for _ in range(T):
  M, N, x, y = map(int, input().split())
  print( solve(M,N,x,y) )
