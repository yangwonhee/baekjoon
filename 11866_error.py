import sys

queue = []
result = []
n, k = map(int, sys.stdin.readline().split())
for i in range(n):
    queue.append(i+1)
k = k -1
first = k
i = 2
while len(queue):
    a = queue.pop(k)
    result.append(a)
    print(result, k)

    if k > len(queue):
        k = (k+1) % len(queue)
    elif 2*i > len(queue):
        k = (2*i) % len(queue)
    else:
        k = 2 * i
    i += 1

print(result)