sum = 0

for i in range(5):
    t = int(input())
    if t < 40:
        t = 40
    sum += t
print(sum // 5)