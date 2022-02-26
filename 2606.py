from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [0] * (n+1)
cnt = 0

def dfs(n):
    global cnt
    check[n] = 1
    for i in graph[n]:
        if not check[i]:
            cnt += 1
            dfs(i)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt)