def Z(n: int, r: int, c: int):
  if n == 0:
    return 0
  half = 2 ** (n-1)
  if r < half and c < half: # 1
    return Z(n-1, r, c)
  if r < half and c >= half:  # 2
    return half*half + Z(n-1, r, c-half)
  if r >= half and c < half:  # 3
    return 2*half*half + Z(n-1, r-half, c)
  if r >= half and c >= half: # 4
    return 3*half*half + Z(n-1, r-half, c-half)

N, r, c = map(int, input().split())

print( Z(N,r,c) )
