import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(list(sys.stdin.readline().split()))

data.sort(key=lambda x : int(x[0]))

for i in range(N):
    print(data[i][0], data[i][1])
