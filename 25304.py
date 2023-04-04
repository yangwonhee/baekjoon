X = int(input())
N = int(input())
all = 0
for i in range(N):
    w, num = map(int, input().split())
    all += w*num
if all == X:
    print("Yes")
else:
    print("No")