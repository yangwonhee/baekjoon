N = int(input())
gong = ' '
st = '*'
for i in range(1, N+1):
    g_cnt = N - i
    st_cnt = i*2 - 1
    print(gong*(g_cnt)+st*st_cnt)

for i in range(N-1, 0, -1):
    g_cnt = N - i
    st_cnt = i*2 - 1
    print(gong*(g_cnt)+st*st_cnt)