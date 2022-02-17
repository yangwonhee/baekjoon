import sys
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

max = max(t)
min = min(t)
print(max * min)