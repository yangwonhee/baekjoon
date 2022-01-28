# N = int(input())

# if (N - 5 * (N / 5)) % 3 == 0:
#     print(int((N / 5) + (N - 5 * (N / 5)) / 3))
# else:
#     for i in range(1,int(N/5)):
#         if (N - 5 * (N / (5-i))) % 3 != 0:
#             print(-1)
#         else:
#             print(int(N / 5)+(N - 5 * (N / (5-i)) / 3))


n = int(input())

result = 0 

while n >= 0:
    if n % 5 == 0:
        result += n // 5
        print(result)
        break
    n -= 3 
    result += 1 
else:
    print(-1)