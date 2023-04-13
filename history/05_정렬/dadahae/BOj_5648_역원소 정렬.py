import sys
input = sys.stdin.readlines
numbers = []

for line in input():
  nums = list(line.split())
  for n in nums:
    numbers.append(int(n[::-1]))

for n in sorted(numbers[1:]):
  print(n)
