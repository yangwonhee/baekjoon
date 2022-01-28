# T = int(input())
# for i in range(T):
#     x, y = map(int, input().split())
#     sum = y-x
#     cnt = 0
#     j = 1
#     dist = 0
#     while sum > dist:
#         cnt += 1
#         dist += j
#         if cnt % 2 == 0:
#             j += 1
#     print(cnt)


T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    count = 0
    distance = 1
    move = 0
    sum = y - x
    while sum > distance:
        count += 1
        distance += move
        if count % 2 == 0:
            move += 1
    print(count)