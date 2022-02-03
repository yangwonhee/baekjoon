import sys
from collections import deque
read = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visit+list