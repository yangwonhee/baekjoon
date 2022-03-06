import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()

for i in range(m):
    count = count_by_range(arr, arr2[i], arr2[i])
    if count:
        print(1)
    else:
        print(0)
    