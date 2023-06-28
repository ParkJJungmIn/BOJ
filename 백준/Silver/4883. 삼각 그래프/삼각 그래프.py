count = 1

while True:
    N = int(input())

    if N == 0:
        break

    dp = [ list(map(int,input().split())) for _ in range(N)]

    dp[1][0] += dp[0][1]
    dp[1][1] += min( dp[1][0], dp[0][1], dp[0][2]+dp[0][1] )
    dp[1][2] += min( dp[1][1], dp[0][1], dp[0][1]+dp[0][2] )

    for i in range(2,N):
        dp[i][0] += min( dp[i-1][0] , dp[i-1][1])
        dp[i][1] += min( dp[i-1][0] , dp[i-1][1], dp[i-1][2] , dp[i][0])
        dp[i][2] += min( dp[i-1][2] , dp[i-1][1], dp[i][1] )
    
    print(f"{count}.", dp[-1][1] )  
    count += 1