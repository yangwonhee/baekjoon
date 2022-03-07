from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
li1= list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))
li1.sort()

start = 0
end = len(li2) - 1
result = 0
data = [0 for _ in range(m)]
print(li1)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(li1, li2[i], 0, n-1) == None:
        print(0, end=" ")
    else:
        print(1, end=" ")