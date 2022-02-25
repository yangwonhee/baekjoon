import sys
from collections import deque

n = int(sys.stdin.readline())
data = deque(map(int, sys.stdin.readline().split()))
stack = []
while len(data) != 0:
    for j in range(1, len(data)-1):
        if data[0] < data[j]:
            stack.append(data[j])
            data.popleft()
            break
        elif data[j] == data[-1] and data[j] < data[0]:
            stack.append(int(-1))
            data.popleft()
            break
        else:
            continue

print(stack)