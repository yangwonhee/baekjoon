from math import sqrt

T = int(input())
max = 5000 + 1
decimal_list = [1] * max
decimal_list[0] = 0
decimal_list[1] = 0
for i in range(2, int(sqrt(max)+1)):
    for j in range(2*i,max,i):
        decimal_list[j] = 0

for i in range(T):
    n = int(input())
    half = n//2
    for j in range(half, 1, -1):
        if decimal_list[n-j] == 1 and decimal_list[j] == 1:
            print(j, n-j)
            break