N,M = map(int, input().split() )

graph = [ [] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split() )
    graph[a].append(b)
    graph[b].append(a)

visited = []

from collections import deque
answer = 0

def bfs(start):
    global answer

    if start in visited:
        return 0
    
    q = deque()
    visited.append(start)
    q.append(start)

    while q:
        a = q.popleft()

        for b in graph[a]:
            if b not in visited:
                visited.append(b)
                q.append(b)
    return 1


for i in range(1,N+1):
    answer += bfs(i)

print(answer)