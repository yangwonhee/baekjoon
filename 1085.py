x,y,w,h = map(int, input().split())

if w-x > x:
    X = x
else:
    X = w-x

if h-y > y:
    Y = y
else:
    Y = h-y

if X > Y:
    print(Y)
else:
    print(X)