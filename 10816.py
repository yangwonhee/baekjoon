from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
sang = list(map(int, input().split()))
cnt = 0

def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

count = []
for i in sang:
    num = count_by_range(card, i, i)
    count.append(num)

for i in range(m):
    print(count[i], end=' ')