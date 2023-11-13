N = int(input())

dp = [ [0] * 10 for _ in range(N)]

for n in range(1,10):
    dp[0][n] = 1

for n in range(1,N):
    for o in range(10):
        if o == 0 :
            dp[n][0] =  dp[n-1][1]
        elif o == 9:
            dp[n][o] = dp[n-1][8]
        else:
            dp[n][o] = dp[n-1][o-1] + dp[n-1][o+1]

print(sum(dp[-1]) % 1000000000)