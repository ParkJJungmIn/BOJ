import sys
input =sys.stdin.readline

N = int(input())
board = [ list(map(int,input().split())) for n in range(N)]
dp = [0] * (N+1)
M = 0
for i in range(N):
    M = max(dp[i], M)
    if board[i][0] + i > N:
        continue
    dp[i+board[i][0]] = max( board[i][1] + M , dp[i+board[i][0]] ) 
print(max(dp))