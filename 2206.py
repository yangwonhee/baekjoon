from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
        graph.append(list(map(int,input())))
# print(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])

def bfs(a, b, t):
    queue.append([a, b, t])
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny, time])
                elif graph[nx][ny] == 1:
                    if time == 0:
                        time += 1
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append([nx,ny, time])
                    else:
                        continue 
    if graph[n-1][m-1] != 0:
        return graph[n-1][m-1]
    else:
        return -1

print(bfs(0, 0, 0))