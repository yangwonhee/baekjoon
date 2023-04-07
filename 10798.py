all_li = []
res = []
for i in range(5):
    st = str(input())
    li = list(st)
    if len(li) < 15:
        sub_li = [" "] * (15-len(li))
        li = li + sub_li
    all_li.append(li)

blank_li = [" "] * 15
for i in range(10):
    all_li.append(blank_li)


for i in range(15):
    for j in range(15):
        if all_li[j][i] == ' ':
            continue
        res.append(all_li[j][i])

print("".join(res))