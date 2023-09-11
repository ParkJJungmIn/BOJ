N = int(input())
nums = list(map(int,input().split()))

dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(i):
        temp = [ nums[t] for t in range(j,i)]
        dp[i] = max(dp[i], dp[j] + abs(max(temp)-min(temp))  )

print(dp[-1])