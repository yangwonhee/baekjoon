max = 0
for i in range(9):
    input_nums = str(input())
    a_list = input_nums.split()
    for j, k in enumerate(a_list):
        if int(k) >= max:
            max = int(k)
            a, b = i+1, j+1


print(max)
print(a, b)