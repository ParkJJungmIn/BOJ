nums = list(input())

dp = [0] * (len(nums)+1)
dp[0] = 1
dp[1] = 1
for i in range(2,len(nums)+1):
    if nums[i-1] != '0':
        dp[i] += dp[i-1]

    if 1 <= int(nums[i-2]+nums[i-1]) <= 26 and nums[i-2] != '0':
        dp[i] += dp[i-2]
    dp[i] %= 1000000

if nums[0] != '0':
    print(dp[-1])
else:
    print(0)