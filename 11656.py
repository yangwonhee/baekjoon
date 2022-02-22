s = str(input())
s_list = []

for _ in s:
    s_list.append(s)
    s = s[1:]
s_list.sort()
for i in s_list:
    print(i)