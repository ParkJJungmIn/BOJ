N,C = map(int, input().split())

nums = [ int(input()) for _ in range(N)]
nums.sort()

left = 1
right = nums[-1] - nums[0]

answer = 0
if C == 2:
    print(right)
    exit()

while left < right:
    mid = (left+right) // 2
    count = 1

    tmp_distance = nums[0]

    for n in range(N):
        if nums[n] - tmp_distance >= mid:
            tmp_distance = nums[n]
            count += 1
    
    if count >= C:
        left = mid+1
        answer = mid
    else:
        right = mid

print(answer)