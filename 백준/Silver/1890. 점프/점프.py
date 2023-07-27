N = int(input())

board = [ list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = 1
# tmp = board[0][0]
# while tmp <= N:
#     dp[tmp][0] = 1
#     tmp += board[tmp][0]

# tmp = board[0][0]
# while tmp <= N:
#     dp[0][tmp] = 1
#     tmp += board[0][tmp]

for y in range(N):
    for x in range(N):
        # [ print(d) for d in dp]
        # print( x,y, x-board[y][x], dp[y][x-board[y][x]],y-board[y][x], dp[y-board[y][x]][x], '==============')
        if dp[y][x] == 0 or (x,y) == (N-1,N-1): continue

        if 0<=x+board[y][x]<N :
            if dp[y][x+board[y][x]] == 0 :
                dp[y][x+board[y][x]] = dp[y][x]
            else:
                dp[y][x+board[y][x]] += dp[y][x]
            # dp[y][x+board[y][x]] = max( dp[y][x+board[y][x]] , dp[y][x] + 1 )
        if 0<=y+board[y][x]<N :
            if dp[y+board[y][x]][x] == 0:
                dp[y+board[y][x]][x] = dp[y][x]
            else:
                dp[y+board[y][x]][x] += dp[y][x]
            # dp[y+board[y][x]][x] = max( dp[y+board[y][x]][x] , dp[y][x]+1 )


print(dp[-1][-1])