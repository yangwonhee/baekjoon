import sys

n = int(sys.stdin.readline())

stairs = [0] * 301
for i in range(n):
    stairs[i] = int(sys.stdin.readline())
dp = [0] * 301

dp[0] = stairs[0]
dp[1]= max(stairs[0]+stairs[1], stairs[1])
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
for i in range(3, n):
    dp[i] = (max(dp[i-2] + stairs[i], dp[i-3]+stairs[i]+stairs[i-1]))

print(dp[n-1])

