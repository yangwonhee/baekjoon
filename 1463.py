import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)

def count(x):
    for i in range(2, x+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+ 1)
    return dp[x]
print(count(n))