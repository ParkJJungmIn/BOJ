N,M = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(M)]

visited = [ float('inf')] * (N+1)
visited[1] = 0
for i in range(1,N+1):
    for j in range(M):
        now, next, cost = graph[j]
        if visited[now] != float('inf') and visited[next] > visited[now] + cost:
            visited[next] = visited[now] + cost
            if i == N:
                print('-1')
                exit()

[ print('-1') if i == float('inf') else print(i) for i in visited[2:] ]