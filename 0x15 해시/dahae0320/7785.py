import sys
input = sys.stdin.readline
n = int(input())
logs = dict()
for _ in range(n):
  name, status = input().strip().split()
  logs[name] = status
for log in sorted(logs.items(), reverse=True):
  if log[1] == "enter":
    print(log[0])
