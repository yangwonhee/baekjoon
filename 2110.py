import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start = 1
end = max(house)
result = 0

while(start <= end):
    mid = (start + end) // 2
    set = house[0]
    count = 1

    for i in house:
        if i >= set+mid:
            count += 1
            set = i
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    

print(result)