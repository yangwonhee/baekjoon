N, M = map(int, input().split())
n_list = [0]*N

for t in range(M):
    i, j, k = map(int, input().split())
    for num in range(i-1, j, 1):
        n_list[num] = k

print(*n_list)