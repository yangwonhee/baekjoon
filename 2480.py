import sys
a, b, c= list(map(int, sys.stdin.readline().split()))

noon = [a, b, c]
noon.sort()

if a == b == c:
    print(10000+a*1000)
elif noon[0] == noon[1] or noon[1] == noon[2]:
    print(1000+noon[1]*100)
else:
    print(noon[2]*100)