import sys
input = sys.stdin.readline
k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in line:
        if x >= mid:
            cnt += x // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)