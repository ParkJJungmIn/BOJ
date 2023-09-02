N = int(input())

dp = [1]*(N+1)
num = [0] + [ int(input()) for _ in range(N)]

for i in range(1,N+1):
    for j in range(1,i):
        if num[j]<num[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(N-max(dp))