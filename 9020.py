# find decimals 2~5000

max = 10002
decimal_list = [True] * max
decimal_list[0] = 0
decimal_list[1] = 0

for i in range(2, max):
    if decimal_list[i]:
        for j in range(i * 2, max, i):
            decimal_list[j] = False

T = int(input())

for i in range(T):
    N = int(input())
    half = N // 2
    for j in range(half, 1, -1):
        if decimal_list[N - j] and decimal_list[j]:
            print(j, N -j)
            break
