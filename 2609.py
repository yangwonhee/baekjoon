n, m = map(int, input().split())

def max(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def min(n, m):
    return n * m // max(n, m)

print(max(n,m))
print(min(n,m))