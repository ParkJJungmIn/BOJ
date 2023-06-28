N = int(input())

tp =  [ list(map(int,input().split())) for _ in range(N)]

dp = [0] * (N+1)


for i in range(N-1, -1,-1) :
    if tp[i][0] + i <= N:
        dp[i] = max( tp[i][1] + dp[ tp[i][0] + i ], dp[i+1] )
    else:
        dp[i] = dp[i+1]

print(dp[0])