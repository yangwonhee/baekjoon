# N = int(input())
# word = []
# new_list = []
# result = 0

# for i in range(N):
#     word = list(input())
#     cnt = 0
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             if new_list.count(word[j]) < 1:
#                 new_list.append(word[j])
#                 print(new_list)
#             else:
#                 cnt += 1
#                 print(cnt)
#     if cnt == 0:
#         result += 1        
#     new_list = []
# print(result)

#############

# N = int(input())
# word = []
# newlist = []
# cnt = 0
# for i in range(N):
#     word[i] = input()
#     for j in word[i]:
#         if newlist.count(j) == 0 :
#             newlist.append(j)
#             if j == len(word[i]):
#                 cnt += 1
#         else:
#             exit()

#############


# N = int(input())
# word = []
# newlist = []
# cnt = 0

# for i in range(N):
#     word = input()
#     for j in i:
#         if newlist.count(j) == 0 :
#             newlist.append(j)
#             print(newlist)
#             if j == len(i):
#                 cnt += 1
        
            
# print(N-cnt)

#########

# N = int(input())
# word = []
# new_list = []
# result = 0

# for i in range(N):
#     word = list(input())
#     cnt = 0
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             new_list.append(word[j+1])
#             for k in new_list:
#                 if word.count(k) >= 1:
#                     cnt += 1
#     if cnt == 0:
#         result += 1        
#     new_list = []

# print(result)



N = int(input())
result = 0
for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result += 1
            break
print(N - result)