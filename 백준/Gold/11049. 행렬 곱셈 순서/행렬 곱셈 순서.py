N = int(input())

mat = [  list( map(int, input().split() )) for _ in range(N)]
dp = [ [0] * N for _ in range(N)]

for point in range(1,N):
    for left in range(N-point):
        right = left + point

        tmp = float('inf')
        for mid in range(left,right):
            tmp = min( tmp, dp[left][mid] + dp[mid+1][right] + mat[left][0] * mat[mid][1] * mat[right][1])

        dp[left][right] = tmp



print( dp[0][-1] )