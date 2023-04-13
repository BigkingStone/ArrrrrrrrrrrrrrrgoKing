N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
idx1 = 0; idx2 = 0
while True:
  if A[idx1] > B[idx2]:
    answer.append(B[idx2])
    idx2 += 1
  else:
    answer.append(A[idx1])
    idx1 += 1
  
  if idx1 >= N:
    answer += B[idx2:]
    break
  if idx2 >= M:
    answer += A[idx1:]
    break

print( " ".join(map(str, answer)) )
