import sys
from collections import deque

t = int(sys.stdin.readline())
deq = deque()

for _ in range(t):
    p = str(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    deque(arr)

    if n == 0:
        arr = []

    check = 0
    time = 0
    for i in p:
        if i == "R":
            time += 1
        elif i == "D":
            if arr:
                if time % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                check = 1
                break

    if check == 0:
        if time % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")