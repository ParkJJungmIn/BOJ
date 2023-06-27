N = int(input())
M = int(input())


dp = [0] * (N+1)

if N == 1:
    print(1)
    exit()

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
pre = 0

if M == 0:
    print(dp[N])
    exit()

for i in range(M):
    cut = int(input())
    answer *= dp[ cut -1 -pre]
    pre = cut
answer *= dp[ N-pre]

print(answer)