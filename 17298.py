from collections import deque
n = int(input())
data = list(map(int, input().split()))
oh_big = [-1] * n
stack = deque()
for i in range(n):
    while stack and stack[-1][0] < data[i]:
        temp, idx = stack.pop()
        oh_big[idx] = data[i]
    stack.append([data[i], i])

print(*oh_big)