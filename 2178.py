from collections import deque

n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < n and 0 <= nb < m and graph[na][nb] == 1:
                graph[na][nb] = graph[a][b] + 1
                queue.append([na, nb])
    return graph[n-1][m-1]

print(bfs(0, 0))