N, M = map(int, input().split())
li = [i for i in range(1, N+1)]
# print(li)
# print(li[1:3])
for cnt in range(M):
    i, j, k = map(int, input().split())
    # a_li = li[i-1:j]
    x_li = li[k-1:j]
    y_li = li[i-1:k-1]
    a_li = x_li + y_li
    li[i-1:j] = a_li
    # print(y_li, x_li, a_li)
    
    
print(*li)