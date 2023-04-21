n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

visited = [False for _ in range(x)]
answer = 0

for i in numbers:
  if i >= x: continue
  if visited[x-i]:
    answer += 1
  visited[i] = True

print(answer)
