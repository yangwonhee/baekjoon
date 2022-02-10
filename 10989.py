# 메모리 초과

import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]

data.sort()

for i in range(N):
    print(data[i])