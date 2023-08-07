N = int(input())
INF = int(1e9)

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for i in range(N)]


def dfs(y, visited):

    if visited == (1 << N)-1:
        return board[y][0] if board[y][0] else INF

    if dp[y][visited] != -1:
        return dp[y][visited]

    for i in range(1, N):
        if visited & (1 << i):
            continue
        if not board[y][i]:
            continue
        
        
        tmp_visited = dfs(i, (1 << i) | visited)
        if dp[y][visited] == -1 :
            dp[y][visited] = tmp_visited + board[y][i]
        else :
            dp[y][visited] = min(dp[y][visited], tmp_visited + board[y][i])

    if dp[y][visited] == -1:
        return INF
    else:
        return dp[y][visited]


print(dfs(0, 1))