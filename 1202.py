import sys
input = sys.stdin.readline
# n = 보석 개수 / k = 가방 개수 (가방에 1개만 담을 수 있음)
n, k = map(int, input().split())
# m = 보석 무게 / v = 보석 가격 / c = 가방 수용 무게
m = [[i] for i in range(n)]
v = [[i] for i in range(n)]
c = []
result = 0
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    m[i].append(a)
    v[i].append(b)
for i in range(k):
    t = int(input())
    c.append(t)

m.sort(key=lambda x: x[1])
v.sort(reverse=True, key=lambda x: x[1])
c.sort(reverse=True)
print(m,v,c)
save = []
while c:
    bag = c.pop()
    for j in m:
        num, kg = j
        if kg <= bag and v[num][1] != 0:
            result += v[num][1]
            v[num][1] = 0
            break


print(result)