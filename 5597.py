li = [0]*31
li[0] = 1
for i in range(28):
    n = int(input())
    li[n] = 1

for i in range(1, 31):
    if li[i] == 0:
        print(i)
# a = [num for num, ele in enumerate(li) if ele == 0]
# print(a)