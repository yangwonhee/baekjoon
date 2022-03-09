import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
data.sort()

start = data[0]
end = data[n-1]
result = m // n

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in data:
        if i <= mid:
            sum += i
        else:
            sum += mid
    if sum <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)