S = str(input())
print(ord("a"), ord("z"), ord("z")-ord("a"))
alphabet = [0 for _ in range(ord("z") - ord("a")+1)]

for s in S:
  alphabet[ord(s)-97] += 1

print(" ".join(map(str, alphabet)))
