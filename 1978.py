N = int(input())
result = 0
num = input().split()
for i in range(N):
    cnt = 0
    ing = int(num[i])
    for k in range(1,ing+1):
        if ing % k == 0:
            cnt += 1
    if cnt == 2:
        result += 1

print(result)