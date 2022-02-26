from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                print(queue)

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)

# graph 내의 list 안의 그 값의 최댓값들을 최댓값에 넣음 계속 반복.. 
