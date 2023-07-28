import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [ [0] * (N) for _ in range(N)]

for point in range(N):
    for left in range(N-point):
        right = point + left

        if left == right :
            dp[left][right] = 1
        elif nums[left] == nums[right]:
            # 1 2 (3 3) 2 1 <- 3 3 같은 경우 처리하기
            if left + 1 == right :
                dp[left][right] = 1
            # 아랫 대각선으로 펠린드롬 성질을 가지고 있는지 판단하기
            elif dp[left+1][right-1] == 1:
                dp[left][right] = 1

for _ in range(M):
    start,end = map(int,input().split())
    print(dp[start-1][end-1])