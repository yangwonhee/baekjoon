dp = [0 for _ in range(13)]
def pick(a, num):
    if num == 6:
        for i in range(6):
            print(dp[i], end=' ')
        print()
        return
    for i in range(a, len(data)):
        dp[num] = data[i]
        pick(i+1, num+1)

while 1:
    data= list(map(int, input().split()))
    if data[0] == 0:
        break
    del data[0]
    pick(0, 0)
    print()