# 야매 연결 리스트
# Python으로 제출하면 시간초과가 나서 Pypy3로 제출함.
MX = 1000005
data = [-1 for _ in range(MX)]
prev = [-1 for _ in range(MX)]
next = [-1 for _ in range(MX)]
unused = 1
cursor = 0

# addr: 각 원소의 주소, 즉 배열 상에서 몇 번지인지를 의미함
def insert(address, element):
  global unused
  data[unused] = element
  prev[unused] = address
  next[unused] = next[address]
  if next[address] != -1: prev[next[address]] = unused
  next[address] = unused
  unused += 1

def erase(address):
  next[prev[address]] = next[address]
  if next[address] != -1: prev[next[address]] = prev[address]

# 0번지에서 출발해 next에 적힌 값을 보고 계속 넘어가면서 data을 출력하는 방식
# cur라는 변수에 각 원소들의 주소가 담겨서 이동하는 방식
def traverse():
  cur = next[0] # 시작 번지
  while cur != -1:
    print(data[cur], end= "")
    cur = next[cur]
  print("")


# --- 문제 풀이 --- #
for char in list(input()):
  insert(cursor, char)
  cursor += 1
size = cursor

for _ in range(int(input())):
  oper = list(input().split())
  if oper[0] == "L":
    if prev[cursor] != -1:  
      cursor = prev[cursor]
  elif oper[0] == "D": 
    if next[cursor] != -1:  
      cursor = next[cursor]
  elif oper[0] == "B":
    if prev[cursor] != -1: 
      erase(cursor)
      cursor = prev[cursor]
  else: # "P" 
    insert(cursor, oper[1])
    cursor = next[cursor]

traverse()
