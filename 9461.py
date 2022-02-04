T = int(input())
case = [1, 1, 1, 2, 2, 3, 4, 5]

def case_push(case, i):
    while i > 7:
        case_push(case[i-6])
        i -= 1
    return case[i-1] + case[i-6]

for i in range(T):
    if i < 7:
        print(case[i])
    else:
        while i > 0:
            print(case_push(case, i))