from math import sqrt
a = [1] *3
b = [1] *3

for i in range(3):
    x, y = map(int, input().split())
    a[i] = x
    b[i] = y

for i in range(3):
    if a.count(a[i]) == 1:
        newx = a[i]
    if b.count(b[i]) == 1:
        newy = b[i]

print(newx, newy)