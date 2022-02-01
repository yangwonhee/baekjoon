n, m = map(int, input().split())


yaksuM = [1,]
yaksuN = [1,]

def max(n, m):
    all = 1
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            yaksuN.append(i)
    yaksuN.append(n)
    

        
    for j in range(2, int(m*0.5) +1):
        if m % j == 0:
                yaksuM.append(j)
    yaksuM.append(m)
    
    if m>n:
        for i in range(len(yaksuM)-1,1,-1):
            if n%yaksuM[i]==0 and m%yaksuM[i]==0:
                return yaksuM[i]
    else:
        for i in range(len(yaksuN)-1,1,-1):
            if n%yaksuN[i]==0 and m%yaksuN[i]==0:
                return yaksuN[i]
    

def min(m, n):
    t = max(n, m)
    a = n // t
    b = m // t


    return a*b*t

print(max(n,m))
print(min(n,m))