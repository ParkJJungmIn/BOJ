N,M = map(int,input().split())

dp = [ [ 0 for _ in range(M+1)] for _ in range(N+1)]
bag = [ 0 ]

for _ in range(N):
    w,v = map(int,input().split())
    bag.append( [w,v] )

for n in range(1,N+1):
    for m in range(1,M+1):
        w = bag[n][0]
        v = bag[n][1]

        if m < w :
            dp[n][m] = dp[n-1][m]
        else:
            dp[n][m] = max( v + dp[n-1][m-w] , dp[n-1][m]  )

print(dp[N][M])