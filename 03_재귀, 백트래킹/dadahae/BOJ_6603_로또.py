import sys
input = sys.stdin.readline

def NandM(k:int, n:int):
  if k == 6:
    print( " ".join(list(map(str, answer))) )
  else:
    st = 0
    if k != 0: st = indexed[answer[k-1]] + 1  # k-1일때 answer에 있는 값보다 큰 숫자들이 와야하므로!!
    for num in numbers[st:]:  # st번째 숫자부터 반복을 돈다. (N과 M(2)번 문제와 사실상 동일함)
      if visited[num] == False:
        answer[k] = num
        visited[num] = True
        NandM(k+1, n)
        visited[num] = False

answer = []
indexed = [-1]*50
visited = [False]

while True:
  line = input().rstrip()
  if line[0] == "0":
    break
  line = list(map(int, line.split())) # 한줄씩 받아야 하므로 readline 사용.
  N = line[0]; numbers = line[1:]
  for i,v in enumerate(numbers):  # numbers의 숫자들은 크기 순으로 정렬되어 있으나 값이 곧 인덱스가 아니므로 
    indexed[v] = i    # indexed 배열에 값-인덱스 를 저장해둠.
  answer = [0]*6
  visited = [False]*50
  NandM(0, N)
  print()
