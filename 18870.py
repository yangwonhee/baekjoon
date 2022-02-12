import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
arr = []

arr = list(sorted(set(data)))

arr2 = {arr[i]:i for i in range(len(arr))}

for i in data:
    print(arr2[i], end=" ")