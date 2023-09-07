N,M,K = map(int, input().split())

graph = [ [0] * (N+1) for _ in range(N+1)]

for i in range(1,K+1):
    a,b,c = map(int, input().split())
    graph[a][b] = c if not graph[a][b] else max(graph[a][b],c)

dp = [ [0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][2] = graph[1][i]

for i in range(1,N+1):
    for j in range(3,M+1):
        for t in range(1,i):
            if graph[t][i] and dp[t][j-1]:
                dp[i][j] = max(dp[i][j], dp[t][j-1] + graph[t][i])

print(max(dp[-1]))