from collections import deque
import sys
deq = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    statement = input().split()

    if len(statement) == 1:
        cmd = statement[0]
    else:
        cmd, x = statement[0], statement[1]

    if cmd == "push_front":
        tmp = [x]
        tmp.extend(deq)
    elif cmd == "push_back":
        deq.append(x)
    elif cmd == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "empty":
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)