N = int(input())
num = [ 2 ** x for x in range(21)]
dp = [ 0 for _ in range(N+1)]
dp[0] = 1
for n in num:
    if N >= n:
        for i in range(n,N+1):
            dp[i] += dp[i-n]%1000000000

print(dp[-1]%1000000000)