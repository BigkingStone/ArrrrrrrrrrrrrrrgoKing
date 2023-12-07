n = int(input().strip())
info = [[] for _ in range(n)]
for i in range(n):
  name, kor, eng, math = input().strip().split()
  info[i] = [int(kor), int(eng), int(math), name]
info.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))
for i in range(n):
  print(info[i][3])
