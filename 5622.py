numlist = input()
apb = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

print(numlist)

for i in numlist:
    for j in apb:
        if i in j:
            time += apb.index(j) + 3


print(time)