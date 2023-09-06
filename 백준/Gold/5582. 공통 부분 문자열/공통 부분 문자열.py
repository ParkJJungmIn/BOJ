now = ['']+list(input())
next = ['']+list(input())

dp = [ [ 0 for __ in range(len(next))] for _ in range(len(now))]

for i in range(1,len(now)):
    for j in range(1,len(next)):
        if now[i] == next[j]:
            dp[i][j] += dp[i-1][j-1] + 1

print( max([ max(d) for d in dp] ))