N,M= map(int,input().split())

byte = [0] + list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))

dp = [ [0] * (sum(costs)+1) for _ in range(N+1) ]

answer = sum(costs)

for i in range(1, N+1):
    b = byte[i]
    c = costs[i]

    for j in range( 1,sum(costs)+1 ):
        if j < c :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max( b + dp[i-1][j-c] , dp[i-1][j])
        
        if M <= dp[i][j]:
            answer = min(answer, j)
    
print(answer)