N,M = map(int,input().split())

graph = [ [ float('inf')] * (N+1) for _ in range(N+1)]


for _ in range(M):
    a,b,c = map(int,input().split())
    if c == 0:
        # graph[b][a] = c
        graph[a][b] = 0
        graph[b][a] = 1
    else:
        graph[a][b]=0
        graph[b][a]=0

Q = int(input())
# print(graph)

for a in range(1,N+1):
    for b in range(1,N+1):
        for c in range(1,N+1):
            # if graph[b][c]
                graph[b][c] = min( graph[b][c] , graph[b][a] + graph[a][c] )

for _ in range(Q):
    a,b = map(int, input().split())
    if a == b:
        print(0)
    else:
        print(graph[a][b])