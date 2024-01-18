import sys
input = sys.stdin.readline
s, e, q = input().strip().split()
sh, sm = list(map(int, s.split(":")))
eh, em = list(map(int, e.split(":")))
qh, qm = list(map(int, q.split(":")))
enter = set()
exit = set()
for line in sys.stdin.readlines():
  t, name = line.strip().split()
  h, m = list(map(int, t.split(":")))
  if h > qh or (h == qh and m > qm): break
  if sh > h or (sh == h and sm >= m): enter.add(name) # 입장 확인
  elif (eh < h or (eh == h and em <= m)) and (qh > h or (qh == h and qm >= m)): exit.add(name)
print(len(enter.intersection(exit)))
