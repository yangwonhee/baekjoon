from collections import deque
import sys
# input = sys.stdin.readline()
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit_1 = [0] * (n+1)
visit_2 = [0] * (n+1)

def dfs(n):
    print(n, end=" ")
    visit_1[n] = 1
    for i in graph[n]:
        if not visit_1[i]:
            dfs(i)

def bfs(n):
    visit_2[n] = 1
    queue = deque([n])
    while queue:
        t = queue.popleft()
        print(t, end=" ")
        for i in graph[t]:
            if not visit_2[i]:
                queue.append(i)
                visit_2[i] = 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)