import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
            elif visited[i] == visited[v]:
                return True
    return True

for _ in range(int(input())):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bi = True

    for i in range(1, V+1):
        if visited[i] == 0:
            bi = dfs(i ,1)
            if not bi:
                break
    
    print("YES" if bi else "NO")