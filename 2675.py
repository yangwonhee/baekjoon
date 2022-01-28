T= int(input())

for i in range(T):
    R, S = input().split()
    text = ""
    for j in S:
        text += j * int(R)
    print(text)