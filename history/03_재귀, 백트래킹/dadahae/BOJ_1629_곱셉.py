def userdefPow(a: int, b: int, c: int) -> int:
  if b == 1:
    return a % c
  val = userdefPow(a, b//2, c)
  val = val * val % c
  if b % 2 == 0:
    return val
  return val * a % c

A, B, C = map(int, input().split())
print( userdefPow(A, B, C) )
