N,M = map(int,input().split())

nums = [  int(input()) for _ in range(M)]

import math

left = 1 
right = max(nums)
answer = max(nums)
while left <= right:
    mid = (left+right) // 2

    count = 0
    for n in nums:
        count += math.ceil( (n / mid))

    if count > N:
        left = mid + 1
    else:
        answer = min(answer, mid)
        right = mid - 1

print(answer)