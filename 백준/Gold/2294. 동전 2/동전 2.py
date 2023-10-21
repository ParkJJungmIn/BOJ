N, M = map(int,input().split())

dp =  [0]+[float('inf')] * (M)  
coin_list = []
for _ in range(N):
    coin_list.append( int(input()) )

for i in range(1,M+1):
    for coin in coin_list:
        if i - coin >= 0:
            dp[i] = min(dp[i-coin]+1, dp[i])
            
print( dp[-1] if dp[-1] != float('inf') else -1 )