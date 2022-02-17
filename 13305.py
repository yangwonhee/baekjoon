import sys
n = int(sys.stdin.readline())
total = 0

far = list(map(int, sys.stdin.readline().split()))
pay = list(map(int, sys.stdin.readline().split()))
minpay = pay[0]


for i in range(n-1):
    if minpay > pay[i]:
        minpay = pay[i]
    total += (minpay * far[i])
print(total)