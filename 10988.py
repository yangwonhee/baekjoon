W = str(input())
li = list(W)
for i, w in enumerate(li):
    if i+1 > len(li) // 2:
        print("1")
        break
    else:
        if w == li[len(li)-i-1]:
            continue
        else:
            print("0")
            break
        