import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data = input()
    data_list = []
    for j in data:
        if j == "(":
            data_list.append("(")
        elif j == ")":
            if len(data_list) != 0 and data_list[-1] == "(":
                data_list.pop()
            else:
                data_list.append(")")
                break

    if len(data_list) == 0:
        print("YES")
    else:
        print("NO")