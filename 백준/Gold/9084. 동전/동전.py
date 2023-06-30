import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M = int(input())
    coin = list(map(int,input().split()))

    result = int(input())

    dp = [0] * (result+1)
    dp[0] = 1
    for c in coin:
        for cc in range(c,result+1):
            dp[cc] += dp[cc-c]
    print(dp[-1])