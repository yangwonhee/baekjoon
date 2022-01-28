data = input().upper()
data_list = list(set(data))
count_list = []

for i in data_list:
    count_list.append(data.count(i))


if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(data_list[count_list.index(max(count_list))])