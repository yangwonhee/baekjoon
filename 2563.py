num = int(input())
white = [[0 for i in range(100)] for i in range(100)]
for i in range(num):
    x, y = map(int, input().split())
    for x1 in range(10):
        for y1 in range(10):
            white[x+x1][y+y1] = 1
    
cnt = 0
for i in range(100):
    for j in range(100):
        if white[i][j] == 0:
            cnt += 1

all = 100*100 - cnt
print(all)