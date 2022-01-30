N = int(input())
i = 2
while N != 1 :
    if N % i == 0:
        print(i)
        N = N / i
        i = 2
        if N == 1:
            break
    else:
        i += 1
