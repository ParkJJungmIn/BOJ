N = int(input())

dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(3,101):
    dp[i] = dp[i-3] + dp[i-2]

for _ in range(N):
    print(dp[int(input()) -1 ])