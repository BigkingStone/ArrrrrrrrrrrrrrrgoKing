def hanoi(a: int, b: int, n: int):
  if n == 1:
    print(a, b)
    return
  hanoi(a, 6-a-b, n-1)
  print(a, b)
  hanoi(6-a-b, b, n-1)

N = int(input())
print( 2**N - 1)
hanoi(1, 3, N)
