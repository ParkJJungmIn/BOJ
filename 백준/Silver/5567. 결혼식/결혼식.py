N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1) ]
visited = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
from collections import deque

visited[1] = 1
q = deque([ 1 ])

while q :
    start = q.popleft()

    for i in graph[start] :
        if visited[i] == 0 :
            q.append(i)
            visited[i] += (visited[start] + 1)

print(len([ i for i in range(2,N+1 ) if 1 <= visited[i] < 4 ]))