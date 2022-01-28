A, B, V = map(int, input().split())
cnt = int((V-B)/(A-B))

if (V-B) % (A-B) == 0:
    print(cnt)
else:
    print(cnt+1)