n_li = []
cnt = 0
all = 0

gr = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F':0.0}

for i in range(20):
    name, num, grade = map(str, input().split())
    if grade == 'P':
        continue
    # all += float(num)
    grade_num = gr[grade]
    all += grade_num * float(num)
    cnt += float(num)


all /= cnt
print("{:.6f}" .format(all))
