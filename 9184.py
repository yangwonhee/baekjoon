import sys
MAX = 21
w_list = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]

def w(a, b, c):
    if a <= 0 or b<=0 or c<=0:
        return 1
    if a >20 or b >20 or c > 20:
        return w(20, 20, 20)

    if w_list[a][b][c]:
        return w_list[a][b][c]

    if a<b<c:
        w_list[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w_list[a][b][c]

    w_list[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1)- w(a-1,b-1,c-1)
    return w_list[a][b][c]

while 1:
    a,b,c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d"%(a, b, c, w(a, b, c)))