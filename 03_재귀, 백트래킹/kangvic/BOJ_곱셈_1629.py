#12^58 mod 67 = 4 -> 12^116(mod 67) = 16
#k승을 구하면 2k승을 구할 수 있고,, 여기에 a를 한번 더 곱하면 2k+1승도 o(1)에 계산할 수 있다.
#함수를,, 어떻게 짜야 할까??
#   처음 1일때 값을 구하고(베이스 값)
# k일때 값이 맞다면 k+1도 성립한다,,처럼 귀납적사고를 통해서 
def pow(a,b,m):
    #베이스 값,, 1일때 나올 값,
    if b == 1: return a % m
    #k를 식을 세운거 처럼,, 12^58 mod 67 = 4 -> 12^116(mod 67) = 16 k승을 구하면 2k승을 구할수 다,, k승의 값을 구하고 그 값에 다시 k승을 곱하면 2k승이 된다.. 
    val = pow(a,b//2,m)
    #2k승
    val = val * val % m
    #b가 짝수라면
		if b%2 == 0: return val
    #홀수라면,, 만약 7이면 2^3이 val에 들어가 결구 2^6이 구해진다.. 따라서 a를 한번 더 곱해줘야한다.
    return val * a % m

a, b, m = map(int, input().split())
print(pow(a,b,m))
