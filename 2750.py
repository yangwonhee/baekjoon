N = int(input())
li = []
for i in range(N):
    t = int(input())
    li.append(t)

li.sort()

for i in range(N):
    print(li[i])