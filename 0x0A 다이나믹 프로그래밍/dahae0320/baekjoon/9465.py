T = int(input())
for _ in range(T):
  n = int(input())
  sticker = []
  d = []
  for i in range(2):
    sticker.append(list(map(int, input().split())))
    d.append([0 for _ in range(n)])
  # 초기값
  d[0][0] = sticker[0][0]
  d[1][0] = sticker[1][0]
  # dp
  for j in range(1, n):
    for i in range(2):
      if j < 2:
        d[i][j] = sticker[i][j] + d[i-1][j-1] if i != 0 else sticker[i][j] + d[i+1][j-1]
      elif i == 0:
        d[i][j] = sticker[i][j] + max(d[i+1][j-1], d[0][j-2], d[1][j-2])
      else:
        d[i][j] = sticker[i][j] + max(d[i-1][j-1], d[0][j-2], d[1][j-2])
  # 최대값
  print(max(d[0][n-1], d[1][n-1]))
