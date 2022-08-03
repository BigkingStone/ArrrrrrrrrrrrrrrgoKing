N = int(input())

def paperCounter(n: int, x: int, y: int):
  tri = n // 3
  flag = False
  for i in range(n):  # (x,y) ~ (x+n, y+n) 까지의 값이 같은지 확인
    for j in range(n):
      if board[x+i][y+j] != board[x][y]:
        flag = True
        break
    if flag:
      break

  if flag:
    paperCounter(tri, x, y)
    paperCounter(tri, x, y+tri)
    paperCounter(tri, x, y+tri*2)
    paperCounter(tri, x+tri, y)
    paperCounter(tri, x+tri, y+tri)
    paperCounter(tri, x+tri, y+tri*2)
    paperCounter(tri, x+tri*2, y)
    paperCounter(tri, x+tri*2, y+tri)
    paperCounter(tri, x+tri*2, y+tri*2)
  else:
    # board[x][y]+1 의 인덱스에 값을 카운트한 이유는 
    # board의 값이 -1부터 1씩 높아지기 때문에.. 
    # 0으로 시작점을 맞추기 위해서이다.
    answer[board[x][y]+1] += 1  
  
answer = [0]*3
board = []
for n in range(N):
  board.append( list(map(int, input().split())) )

paperCounter(N, 0, 0)

for i in answer:
  print(i)