N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
answer = 0

for num in numbers:
  if num == v:
    answer += 1

print(answer)
