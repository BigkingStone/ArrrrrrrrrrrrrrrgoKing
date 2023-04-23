from collections import deque

# test case
for _ in range(int(input())):
  left = deque()
  right = deque()
  for char in input():
    if char == "-":
      if len(left) != 0: left.pop()
    elif char == "<":
      if len(left) != 0: right.appendleft(left.pop())
    elif char == ">":
      if len(right) != 0: left.append(right.popleft())
    else:
      left.append(char)
  print("".join(left+right))
