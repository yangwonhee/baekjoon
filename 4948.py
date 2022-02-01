from math import sqrt

max = 123456 * 2 + 1
T = [True] * max
# print(type(T))
for i in range(2, int(sqrt(max)+1)):
    for j in range(2*i,max,i):
        T[j] = False



def countPrime(num):
    cnt = 0
    for i in range(num+1, num*2+1):
        if T[i]:
            cnt += 1
    print(cnt)

while True:
    num = int(input())
    if num == 0:
        break
    countPrime(num)