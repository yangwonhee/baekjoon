import sys
N, M = list(map(int, sys.stdin.readline().split()))
data = []
def dfs():
    if len(data) == M:
        if data == sorted(data):
            print(" ".join(map(str, data)))
            return
    for i in range(1, N+1):
        if i not in data:
            data.append(i)
            dfs()
            data.pop()

dfs()
