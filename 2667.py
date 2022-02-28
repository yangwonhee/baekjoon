import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, input())) for _ in range(n)]
check = [0] *(n+1)
cnt = 0
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    cnt = 1
    graph[a][b] = 0
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
    return cnt

queue2 = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue2.append(bfs(i, j))

queue2.sort()
print(len(queue2))
for i in range(len(queue2)):
    print(queue2[i])