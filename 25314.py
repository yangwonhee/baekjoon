N = int(input())
if N == 4:
    print("long int")
else:
    a = N//4
    pr = "long " * a
    print(pr+ "int")