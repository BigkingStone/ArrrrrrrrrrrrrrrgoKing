import sys
input = sys.stdin.readline

dp = [0 for i in range(13)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(dp[i], end=' ')
        print()
        return
    for i in range(start, len(arr)):
        dp[depth] = arr[i]
        dfs(i + 1, depth + 1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    dfs(0, 0)
    print()
