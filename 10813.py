N, M = map(int, input().split())
n_list = []
for num in range(1, N+1):
    n_list.append(num)
# print(n_list)
for times in range(M):
    i, j = map(int, input().split())
    t= n_list[i-1]
    n_list[i-1] = n_list[j-1]
    n_list[j-1] = t

print(*n_list)