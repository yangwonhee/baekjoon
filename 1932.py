import sys
input = sys.stdin.readline

n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

k = 2 # ?
for i in range(1, n):
    for j in range(k):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    k += 1
print(max(tri[n-1]))