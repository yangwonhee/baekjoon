import sys
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))
li = [0]

print(case) 

for i in case:
    if li[-1] < i:
        li.append(i)