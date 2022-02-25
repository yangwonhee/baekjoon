import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    data = sys.stdin.readline().split()
    if data[0] == "push":
        queue.append(data[1])
    elif data[0] == "pop":
        if len(queue):
            t = queue.popleft()
            print(t)
        else:
            print("-1")
    elif data[0] == "size":
        print(len(queue))
    elif data[0] == "empty":
        if len(queue):
            print("0")
        else:
            print("1")
    elif data[0] == "front":
        if len(queue):
            print(queue[0])
        else:
            print("-1")
    elif data[0] == "back":
        if len(queue):
            print(queue[-1])
        else:
            print("-1")