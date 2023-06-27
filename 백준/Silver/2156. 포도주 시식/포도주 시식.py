N = int(input())

dp = [0] * N
info = []

for _ in range(N):
    info.append(int(input()))
    
if len(dp) <= 3:
    if N <= 2:
        print( sum(info) )
    else:
        print( max( info[0] + info[2], info[2] + info[1], info[0] + info[1] ) )
    exit()
    
dp[0] = info[0]
dp[1] = info[0] + info[1]
dp[2] = max( info[0] + info[2], info[2] + info[1], dp[1])



for i in range(3,N):
    dp[i] = max( info[i] + dp[i-2], dp[i-3] + info[i] + info[i-1] , dp[i-1] )

print(dp[-1])