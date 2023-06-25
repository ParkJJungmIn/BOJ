import sys
input = sys.stdin.readline

N = int(input())
graph = [ [] for n in range(N+1)]
for _ in range(N-1):
    a,b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [ 0 for _ in range(N+1)]
q = [ 1 ]
while q:
    now = q.pop()
    for next in graph[now]:
        if visited[next] == 0:
            visited[next] = now
            q.append(next)

print(*visited[2:])