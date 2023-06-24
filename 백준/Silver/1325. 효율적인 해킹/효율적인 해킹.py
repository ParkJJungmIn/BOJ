N , M= map(int , input().split() )

graph = [ [] for _ in range(N+1)]

for _ in  range(M):
    a,b = map(int , input().split() )
    graph[b].append(a)


from collections import deque
def bfs(start):
    visited = [ False for _ in range(N+1)]
    q = deque( [ start])
    visited[start] = True
    cnt = 1
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] == False:
                visited[next] = 1
                q.append(next)
                cnt += 1
    return cnt

m = -1
answer = []
for i in range(1,N+1):
    tmp_m = bfs(i)
    if tmp_m > m:
        m = tmp_m
        answer = [ i ]
    elif tmp_m == m:
        answer.append( i )

print( *answer )