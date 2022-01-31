def pic(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i%len(n)] + " "*len(n)+ n[i%len(n)])
        else:
            matrix.append(n[i%len(n)] * 3)
    return matrix


N = int(input())
star = ["***", "* *", "***"]
e = 0

while N != 3:
    N = N // 3
    e += 1

for i in range(e):
    star = pic(star)

for i in star:
    print(i)

# N = int(input())
# Matrix = [[0 for i in range(N)] for j in range(N)]

# def star(N):
    

#     # Matrix[1][1] = True
#     return N//3

# star(N)
# for i in Matrix:
#     for j in i:
#         if j == 0:
#             print("*", end=" ")
#         else:
#             print(" ")
