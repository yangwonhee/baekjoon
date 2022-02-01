n, m = map(int, input().split())


yaksuM = [1,]
yaksuN = [1,]
prime = []
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(1, 101):
    if isPrime(i):
        prime.append(i)

if n < m:
    l = n
    n = m
    m = l

def max(n, m):
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            yaksuN.append(i)
    
    for j in range(2, int(m*0.5) +1):
        if m % j == 0 and yaksuN.count(j) == 1:
                yaksuM.append(j)
    all = 1
    for k in range(len(yaksuM)):
        if prime.count(yaksuM[k]) == 1:
            all *= yaksuM[k]
    return all

def min(m, n):
    t = max(n, m)
    a = n // t
    b = m // t
    return a*b*t

if m == 0:
    print(0)
    print(0)
elif m == 1:
    print(1)
    print(n)
elif n == m:
    print(n)
    print(n)
else:
    print(max(n,m))
    print(min(n,m))