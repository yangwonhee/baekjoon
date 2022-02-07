import sys

N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(N)]

data.sort()

for i in range(N):
    print(data[i])