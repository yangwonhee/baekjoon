import sys

n = int(sys.stdin.readline())
data = [0] * 15
result = 0
def dfs(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        data[x] = i
        if check(x):
            dfs(x+1)

def check(x):
    for i in range(x):
        if data[x] == data[i] or abs(data[x]-data[i])==x-i:
            return False
    return True

dfs(0)
print(result)