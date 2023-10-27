# N : 돌 전체, M : 접근불가능 돌 갯수, 접근 불가능한 stone_set

def get_min_jumps(N, M, stone_set):

    # 최대 점프할 수 있는 거리 
    max_jump = int((2 * N) ** 0.5) + 2
    
    dp = [[float('inf')] * max_jump for _ in range(N + 1)]
    dp[1][0] = 0

    for i in range(2, N + 1):
        if i in stone_set:
            continue
        
        for j in range(1, int((2 * i) ** 0.5) + 1):
            # dp[i] : 돌의 갯수 , dp[i][j] 최대 점프갯수
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        #     print('change == ', i,j)
        # [ print(d) for d in dp]
        # print(int((2 * i) ** 0.5) + 1 , '===============')

    return min(dp[N])


N, M = map(int, input().split())

stone_set = set()
for _ in range(M):
    stone_set.add(int(input()))

result = get_min_jumps(N, M, stone_set)

if result == float('inf'):
    print(-1)
else:
    print(result)