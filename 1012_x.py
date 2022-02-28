t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(m, n, k):
    bchu = [list(map(int, input().split())) for _ in range(k)]
    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # for i in range(n):
    #     for j in range(m):
    #         if bchu.count([i,j]) == 1:
    #             graph[i][j] = 1
    for i in bchu:
        x, y = i
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < m and 0 <= ny < n and bchu.count([nx, ny]) == 1:
                graph[nx][ny] = 0


queue = []
for i in range(t):
    m, n, k = map(int, input().split())
    queue.append(dfs(m, n, k))
    result = 0
    for j in range(len(queue)):
        if queue[j] == True:
            result += 1
    print(result)

# graph = [[0 for _ in range(m)] for _ in range(n)]
# for i in bchu:
#     [a, b] = i