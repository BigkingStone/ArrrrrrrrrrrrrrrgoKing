string1 = list(input())
string2 = list(input())
length = len(string1) + len(string2)
same = []

for alphabet in string1:
  if alphabet in string2:
    same.append(alphabet)
    string2.pop(string2.index(alphabet))

print(length - len(same)*2)
