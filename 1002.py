from math import sqrt
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2,r2 = map(int, input().split())
    dist = sqrt((x2-x1)**2 +(y2-y1)**2)
    R = [r1,r2,dist]
    R.sort()
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist == r1+r2 or R[0]+R[1] == R[2]:
        print(1)
    elif R[0]+R[1]< R[2]:
        print(0)
    else:
        print(2)