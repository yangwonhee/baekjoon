import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

if B+C < 60:
    print(A, B+C)
else:
    min = B+C
    hour = min // 60
    min = min % 60
    if A+hour < 24:
        print(A+hour, min)
    else:
        print(A+hour-24, min)



    