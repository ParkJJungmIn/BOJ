import sys
input = sys.stdin.readline
N = int(input())
total = sum([ i for i in range(1,N+1)])
dp = []

for i in range(N):
    dp.append( list(map(int,(input().split()))) )

if N == 1:
    print(dp[0][0])
    exit()

dp[1][0] += dp[0][0]
dp[1][1] += dp[0][0]

if N == 2:
    print(max( dp[-1] ) )
    exit()


for  i in range(2,N):
    before = len(dp[i])
    start = 0
    for j in range(len(dp[i])):
        if j == 0 :
            dp[i][j] += dp[i-1][0]
        elif j == len(dp[i])-1 :
            dp[i][j] += dp[i-1][-1]
        else:
            dp[i][j] = max( dp[i][j] + dp[i-1][start] ,  dp[i][j] + dp[i-1][start+1])
            start += 1

print(max( dp[-1] ) )