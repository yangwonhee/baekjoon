N, M = map(int, input().split())
li = [i for i in range(1, N+1)]
for times in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if j - i == 1:
        t = li[j]
        li[j] = li[i]
        li[i] = t
    elif i == j:
        continue
    else:
        mok = (j-i)//2
        for cnt in range(0, mok+1):
            t = li[j-cnt]
            li[j-cnt] = li[i+cnt]
            li[i+cnt] = t
    # print(*li)
    
print(*li)