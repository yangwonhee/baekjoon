T = int(input())

for i in range(T):
    floor = int(input())
    room = int(input())
    peo = [x for x in range(1, room+1)]
    for j in range(floor):
        for k in range(1, room):
            peo[k] += peo[k-1]
    print(peo[-1])