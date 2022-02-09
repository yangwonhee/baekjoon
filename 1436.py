N = int(input())

end = str(666)
end_list = []

for i in range(1000):
    i = str(i)

    num1 = i + end
    num2 = end + i
    number1 = int(num1)
    number2 = int(num2)

    if '6' in i == 0:
        print(i)
        for j in range(10):
            j = str(j)
            num3 = i + end - '6' + j
            number3 = int(num3)
            end_list.append(number3)

    end_list.append(number1)
    end_list.append(number2)

# list(set(end_list))
# end_list.sort()
# for i in range(N):
#     print(end_list[i])
print("return", end_list[N-1])

# new_list = []
# for i in end_list:
#     if i not in new_list:
#         new_list.append(i)
# new_list.sort()
# print(new_list[N-1])
