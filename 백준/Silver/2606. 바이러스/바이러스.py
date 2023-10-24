from collections import defaultdict

N =  int(input())
M = int(input())

graph = defaultdict(list)

for _ in range(M):
    a,b = map(int, input().split() )
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
stack = [1]

while stack:
    node = stack.pop()
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0 :
            stack.append(n)

print(visited.count(1)-1)