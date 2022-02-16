import re
import sys
n = int(sys.stdin.readline())
sum = 0
people = list(map(int, sys.stdin.readline().split()))
people.sort(reverse=True)

for i in range(1, n+1):
    sum += (people[i-1] * i)

print(sum)