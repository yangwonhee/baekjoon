data = input().upper()
data_list = list(set(data))
count_list = []
cnt = 0

for i in data_list:
    cnt = data.count(i)
    count_list.append(cnt)


if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(data_list[count_list.index(max(count_list))])