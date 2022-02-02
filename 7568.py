n = int(input())
nlist = []
for i in range(n):
    nlist.append(list(map(int, input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if nlist[i][0] < nlist[j][0] and nlist[i][1] < nlist[j][1]:
            rank += 1
    print(rank, end=" ")