n = int(input())
arr = []
tmp = [0]*1000001

for i in range(n):
    arr.append(list(input().split()))
    arr[i][0] = int(arr[i][0])

def merge(st,en):
    mid = (st+en)//2
    lidx = st #arr[st:mid]에서 값을 보기 위해 사용하는 index
    ridx = mid #arr[mid:en]에서 값을 보기 위해 사용하는 index
    for i in range(st, en):
        if ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif lidx == mid: 
            tmp[i] = arr[ridx]
            ridx += 1
        elif arr[lidx][0] <= arr[ridx][0]:
            tmp[i] = arr[lidx]
            lidx += 1
        else: 
            tmp[i] = arr[ridx]
            ridx += 1
    for i in range(st,en): arr[i] = tmp[i]
    
def merge_sort(st,en):
    if en == st + 1: return # 리스트의 길이가 1인 경우
    mid = (st+en)//2
    merge_sort(st, mid)# arr[st:mid]을 정렬
    merge_sort(mid, en)# arr[mid:en]을 정렬
    merge(st, en)# arr[st:mid]와 arr[mid:en]을 합친다.

merge_sort(0,n)
for i in range(n):
    print(arr[i][0], end = " ")
    print(arr[i][1])
