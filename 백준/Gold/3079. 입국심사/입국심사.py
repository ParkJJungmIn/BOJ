N,M = map(int, input().split())

nums = [ int(input()) for _ in range(N)]

left = min(nums)
right = max(nums) * M
answer = float('inf')
while left <= right:
    mid = (left + right) // 2

    count = 0
    for n in nums:
        count += (mid // n)

    if count >= M:
        right = mid -1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)