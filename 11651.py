import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    data.append([b, a])

data.sort()

for i in range(N):
    print(data[i][1], data[i][0])