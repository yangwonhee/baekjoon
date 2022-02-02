N = int(input())
ans = N
nlist = []
for i in range(9, -1, -1):
    nlist.clear()
    nlist.append(str(i))
    for j in range(9, -1, -1):
        nlist.append(str(j))
        for k in range(9, -1, -1):
            nlist.append(str(k))
            if N != i + j + k + int("".join(nlist)):
                nlist.pop()
                continue
            else:
                ans = min(ans, int("".join(nlist)))
        nlist.pop()

if ans != N:
    print(ans)
else:
    print(0)