import sys
from collections import deque
input = sys.stdin.readline
data = []

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    queue.append([sx, sy])
    while queue:
        a, b = queue.popleft()
        if a == fx and b == fy:
            return graph[fx][fy]
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
                graph[x][y] = graph[a][b] + 1
                queue.append([x, y])
        

t = int(input())

for i in range(t):
    print(bfs())