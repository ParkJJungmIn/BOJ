import sys
input = sys.stdin.readline

N = int(input())

max_dp = [ list(map(int,input().split())) for _ in range(N)]
min_dp = [ d[:] for d in max_dp]

item = [ [0,1] , [0,1,2] , [1,2]]

for i in range(1,N):

    for ij in range(3):
            if ij == 0:
                max_dp[i][ij] += max( max_dp[i-1][ij], max_dp[i-1][ij+1])
                min_dp[i][ij] += min( min_dp[i-1][ij], min_dp[i-1][ij+1])
            elif ij == 1:
                max_dp[i][ij] += max( max_dp[i-1][ij], max_dp[i-1][ij+1], max_dp[i-1][ij-1])
                min_dp[i][ij] += min( min_dp[i-1][ij], min_dp[i-1][ij+1], min_dp[i-1][ij-1])
            else:
                max_dp[i][ij] += max( max_dp[i-1][ij], max_dp[i-1][ij-1])
                min_dp[i][ij] += min( min_dp[i-1][ij], min_dp[i-1][ij-1])

print(max(max_dp[-1]), min(min_dp[-1]))