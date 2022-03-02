from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    check = [[[0] *2 for _ in range(m)]for _ in range(n)]
    check[0][0][1] = 1
    while queue:
        x, y, k = queue.popleft()
        if x == n-1 and y == m-1:
            return check[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and k == 1:
                        check[nx][ny][0] = check[x][y][1] + 1
                        queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and check[nx][ny][k] == 0:
                    check[nx][ny][k] = check[x][y][k] + 1
                    queue.append([nx, ny, k])
    return -1


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,list(input().strip()))))

print(bfs())