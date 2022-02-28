import sys
n = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = []
a = 0
b = 0

def cut(x, y, n):
    global a, b
    check = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != p[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check == 0:
        a += 1
    else:
        b += 1

cut(0, 0, n)
print(a)
print(b)