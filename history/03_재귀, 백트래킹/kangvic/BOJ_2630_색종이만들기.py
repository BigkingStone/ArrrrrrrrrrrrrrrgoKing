import sys
n=int(sys.stdin.readline())
 
color_paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]#x행 y열
 
white=0#0이면 흰생
blue=0#1이면 파란색
 
def cut(x,y,n):
    global blue,white
    check=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=color_paper[i][j]:#하나라도 같은색이 아니라면
                #4등분
                cut(x,y,n//2)#1사분면
                cut(x,y+n//2,n//2)#2사분면
                cut(x+n//2,y,n//2)#3사분면
                cut(x+n//2,y+n//2,n//2)#4사분면
                return
 
 
    if check==0:#모두 흰색일때
        white+=1
        return
    else:   #모두 파란색일때
        blue+=1
        return
 
 
cut(0,0,n)
print(white)
print(blue)
