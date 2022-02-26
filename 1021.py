import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
deq = deque()
cnt = 0

deq = deque([i for i in range(1, n+1)])


for i in data:
    while 1:
        if deq[0] == i: 
            deq.popleft()
            break
        else:
            if deq.index(i) < len(deq)/2:
                while deq[0] != i:
                    deq.append(deq.popleft())
                    cnt += 1
            else:
                while deq[0] != i:
                    deq.appendleft(deq.pop())
                    cnt += 1
print(cnt)
# print("deq:",deq)