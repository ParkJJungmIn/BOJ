N,M = map(int,input().split())

dp = [[ [0] + [ -float('inf') for _ in range(M)] for _ in range(N+1) ] for _ in range(2)] 

nums = [0] + [ int(input()) for _ in range(N)]
for i in range(1,N+1):
    for j in range(1, min(M, i//2+2) + 1 ):
        dp[1][i][j] = max( dp[0][i-1][j] , dp[1][i-1][j])
        dp[0][i][j] = max( dp[0][i-1][j] , dp[1][i-1][j-1]) + nums[i]

print(max(dp[0][N][M] , dp[1][N][M] ) )