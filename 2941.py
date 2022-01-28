croalpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()

for i in croalpa:
    data = data.replace(i,"^")

print(len(data))



# new_list = []

# for i in croalpa:
#     if i in data:
#         new_list.append(i)


# print(len(new_list))