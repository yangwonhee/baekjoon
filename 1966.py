import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    data_list = [0 for _ in range(n)]
    data_list[m] = 1
    cnt = 0
    while True:
        if data[0] == max(data):
            cnt += 1
            if data_list[0] == 1:
                print(cnt)
                break
            else:
                data.pop(0)
                data_list.pop(0)
        else:
            data.append(data[0])
            del data[0]
            data_list.append(data_list[0])
            del data_list[0]