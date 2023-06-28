N = int(input())

dp = [0] * 1000001

if N <= 2:
    print([1,2][N-1])
    exit()

dp[0] = 1
dp[1] = 2

for i in range(2,1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N-1])