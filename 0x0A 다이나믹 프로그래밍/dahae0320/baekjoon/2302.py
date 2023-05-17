N = int(input())  # 좌석의 개수
M = int(input())  # 좌석을 예약한 VIP 회원들의 수
d = [0 for _ in range(N+1)] # 사람들이 i번 좌석까지 앉는 서로 다른 방법의 가짓수
s = [0 for _ in range(N+1)] # VIP 회원들이 없을 때, 사람들이 i번 좌석까지 앉는 서로 다른 방법의 가짓수
normal = 0  # VIP 석 다음에 위치한 일반 좌석을 예약한 손님의 수
isvip = [False for i in range(N+1)] # VIP 회원이 예약한 좌석
for i in range(M):
  isvip[int(input())] = True
# 초기화
d[0] = d[1] = 1
s[0] = s[1] = 1
# dp
for i in range(1,N+1):
  s[i] = s[i-1] + s[i-2] if i > 1 else s[i]
  normal += 1
  if isvip[i]:
    d[i] = d[i-1]
    normal = 0
  elif normal == i:
    d[i] = s[normal]
  else:
    d[i] = d[i-normal] * s[normal]
# N번 좌석까지 사람들이 앉을 수 있는 서로 다른 방법의 가짓수는?
print(d[N])
