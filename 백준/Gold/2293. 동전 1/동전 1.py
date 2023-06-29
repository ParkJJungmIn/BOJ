N,M = map(int,input().split())

dp = [0] * (M+1)
dp[0] = 1

coin = [ int(input()) for _ in range(N)]

for c in coin:
    for cc in range(c,M+1):
        dp[cc] += dp[cc-c]

print(dp[-1])