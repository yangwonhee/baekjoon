import sys
N, M = list(map(int, sys.stdin.readline().split()))
data = []
def dfs(a):
    if len(data) == M:
        print(" ".join(map(str, data)))
        return
    for i in range(a, N+1):
        data.append(i)
        dfs(i)
        data.pop()

dfs(1)