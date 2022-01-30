M, N = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)

# for i in range(M, N-M+2):
#     cnt = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             cnt += 1
#             if cnt > 2:
#                 break
#     if cnt == 2:
#         decimal_list.append(i)

# for i in decimal_list:
#     print(i)