# # 메모리 초과

# import sys
# N = int(sys.stdin.readline())
# data = [int(sys.stdin.readline()) for _ in range(N)]

# data.sort()

# for i in range(N):
#     print(data[i])

import sys

N = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(N):
    data[int(sys.stdin.readline())] += 1

for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)