while 1:
    data = list(map(int, input().rstrip().split()))
    q = []
    if data[0] == 0:
        break
    max = len(data)
    height = max(data)
    for h in range(2, height+1):
        for i in data:
            if i > h:
                if data[i+1] > 2:
                    q.append(i)
        sq = (len(q)+1) * h
        max = max(max, sq)
    
    print(max)