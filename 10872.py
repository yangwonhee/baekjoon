# 이건 좀 그렇겠지 ㅎ
# from math import factorial
# N = int(input())

# if N == 0:
#     print(1)
# else:
#     print(factorial(N))

N = int(input())

def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fac(N-1)
    

print(fac(N))