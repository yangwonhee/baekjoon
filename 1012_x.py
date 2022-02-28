from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for l in range(n):
        for p in range(m):
            if graph[l][p] == 1:
                bfs(l, p)
                graph[l][p] = 0
                count += 1

    print(count)