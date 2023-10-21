N,M,start =  map(int, input().split() )

graph = [ [0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

from collections import deque

def bfs(start, visited):

  stack = deque()
  stack.append(start)
  visited[start] = 1
  while stack :
    node = stack.popleft()
    print(node, end=' ')
    for n in range(N+1):
      if graph[node][n] == 1 and visited[n] == 0:
        visited[n] = 1
        stack.append(n)

def dfs(start, visited):

  visited[start] = 1
  print(start , end = ' ')
  for n in range(N+1) :
    if visited[n] == 0 and graph[start][n] == 1:
      dfs(n,visited)

dfs(start, [ 0 for _ in range(N+1)] )
print()
bfs(start, [ 0 for _ in range(N+1)] )


