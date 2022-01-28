A, B= map(list,input().split())

A.reverse()
B.reverse()
a = int(''.join(A))
b = int(''.join(B))
if a > b:
    print(a)
else:
    print(b)
