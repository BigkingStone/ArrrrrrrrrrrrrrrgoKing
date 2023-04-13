S = input()
zero_chunck = 0
one_chunck = 0

for i in range(0, len(S)-1):
  if S[i] == S[i+1]:
    continue
  if S[i] == '0':
    zero_chunck += 1
  else:
    one_chunck += 1

if S[-1] == '0':
  zero_chunck += 1
else:
  one_chunck += 1

print(min(zero_chunck,one_chunck))
