# 문제 .. 잘못 품 ... 

import sys
t = int(sys.stdin.readline())
MAX = 40
data = [[0, 0] for i in range(MAX)]
data[0] = [1,0]
data[1] = [0,1]
data[3] = [1,2]

def fibo(n):
    if data[n] != [0,0]:
        return data[n]
    else:
        return list(map(lambda a, b: a+b, fibo(n-1), fibo(n-2)))


for _ in range(t):
    n = int(sys.stdin.readline())
    print(fibo(n))