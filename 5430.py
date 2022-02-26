import sys
from collections import deque

t = int(sys.stdin.readline())
deq = deque()

for _ in range(t):
    p = str(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    cnt = 0
    for i in p:
        if i == "R":
            arr.reverse()
        elif i == "D":
            if arr:
                arr.popleft()
            else:
                print("error")
                cnt = 1
                break
    if cnt == 0:
        print("["+",".join(arr)+"]")