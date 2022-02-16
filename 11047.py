import sys

n, k = map(int, sys.stdin.readline().split())
data = []
cnt = 0

for _ in range(n):
    dong = int(sys.stdin.readline())
    data.append(dong)


data.sort(reverse=True)

for i in data:
    if k >= i:
        cnt += (k // i)
        k = k % i
        if k <= 0:
            break
    else: 
        continue

print(cnt)