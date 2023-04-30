import sys
input = sys.stdin.readline  

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = 0
#정렬
arr.sort()
#right, left
right = 0
left = n-1
while right < left:
    if arr[right] + arr[left] > x:
        left -= 1
    elif arr[right] + arr[left] < x:
        right += 1 
    else:
        count += 1
        right += 1
        left -= 1
print(count)
