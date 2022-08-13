#####좌표 정렬
#입력 받기
n = int(input())
arr = []
tmp = [0]*1000001
for i in range(n):
    arr.append(list(map(int, input().split())))
def merge(st,en):
    mid = (st+en)//2
    lidx = st
    ridx = mid
    for i in range(st,en):
        if lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif arr[lidx][0] <= arr[ridx][0]:
            if arr[lidx][0] == arr[ridx][0]:
                if arr[lidx][1] <= arr[ridx][1]:
                    tmp[i] = arr[lidx]
                    lidx+=1
                else: 
                    tmp[i] = arr[ridx]
                    ridx += 1
            else:
                tmp[i] = arr[lidx]
                lidx += 1
        else:
            tmp[i] = arr[ridx]
            ridx += 1
    for i in range(st,en):
        arr[i] = tmp[i]

def merge_sort(st,en):
    if en == st+1: return
    mid = (st+en)//2
    merge_sort(st,mid)
    merge_sort(mid,en)
    merge(st,en)
merge_sort(0,n)
for i in range(n):
    print(arr[i][0],end=' ')
    print(arr[i][1])
