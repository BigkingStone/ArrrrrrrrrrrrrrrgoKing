t = 1
while True:
  L,P,V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  ans = L * (V//P)
  ans += V%P if V%P <= L else L
  print("Case %d: %d" %(t, ans))
  t += 1
