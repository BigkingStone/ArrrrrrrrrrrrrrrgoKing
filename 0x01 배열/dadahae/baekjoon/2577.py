result = 1
numbers = [0 for _ in range(10)]

for _ in range(3):
  result = result * int(input())

for num in str(result):
  numbers[int(num)] += 1

print("\n".join(map(str,numbers)))
