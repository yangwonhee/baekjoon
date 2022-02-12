import sys
N, M = list(map(int, sys.stdin.readline().split()))
data = []
def dfs():
    if len(data) == M:
        print(" ".join(map(str, data)))
        return

    for i in range(1, N+1):
        data.append(i)
        dfs()
        data.pop()

dfs()