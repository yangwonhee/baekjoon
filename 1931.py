import sys

n = int(sys.stdin.readline())
time = []
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time_list = sorted(time, key=lambda x: x[0])
# time_list = sorted(time, key=lambda x: x[1] - x[0])
time_list = sorted(time_list, key=lambda x: x[1])

cnt = 0
limit = 0

for i, j in time_list:
    if i >= limit:
        cnt += 1
        limit = j
print(cnt)