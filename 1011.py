T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    sum = y-x
    cnt = 0
    j = 1
    dist = 0
    while sum > dist:
        cnt += 1
        dist += j
        if cnt % 2 == 0:
            j += 1
    print(cnt)