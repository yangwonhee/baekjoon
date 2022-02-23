import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        data.pop()
    else:
        data.append(a)
sum = 0
for i in range(len(data)):
    sum += data[i]

print(sum)