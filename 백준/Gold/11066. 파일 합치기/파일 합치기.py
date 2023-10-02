N = int(input())

for _ in range(N):
    total = int(input())
    num_list = [0] + list(map(int,input().split() ))

    prefix_sum = [0]

    for i in range(1,len(num_list)):
        prefix_sum.append( prefix_sum[-1] + num_list[i])

    dp = [ [0] * len(num_list) for _ in range(len(num_list)) ]

    for length in range(2, total+1):
        for start in range( 1, total-length+2):
            end = start + length - 1
            dp[start][end] = min( [ dp[start][mid] + dp[mid+1][end] for mid in range(start,end)] ) + prefix_sum[end] - prefix_sum[start-1]
    print(dp[1][-1])