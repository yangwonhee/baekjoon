import sys
from collections import deque

queue = deque()
result = []

n, k = map(int, sys.stdin.readline().split())

for i in range(n):
    queue.append(i+1)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
for i in range(len(result) -1):
    print("%d," %result[i], end=" ")
print(result[-1], end="")
print(">")