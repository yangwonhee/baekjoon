from collections import deque
MAX = 100000
dist = [0] * (MAX+1)
n, k = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        move = [x-1, x+1, x*2]
        for nx in move:
            if 0<= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

bfs()