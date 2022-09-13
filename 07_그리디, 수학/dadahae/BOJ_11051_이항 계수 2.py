n, k = map(int, input().split())
ans = 1
for i in range(n, n-k, -1):
    ans = ans * i
for i in range(1, k+1):
    ans = ans // i
print(ans%10007)
