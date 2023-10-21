from collections import defaultdict

from heapq import heappush, heappop

graph = defaultdict(list)


N,M,K,S = map(int, input().split())

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [float('inf')] * (N+1)

h = []
heappush(h, (0,S))

while h:
    cost, now = heappop(h)

    if visited[now] > cost:
        visited[now] = cost

    for next in graph[now]:
        if visited[next] > cost:
            heappush(h, (cost+1, next))
answer = []
for i in range(1,N+1):
    if visited[i] == K:
        answer.append(i)

if answer:
    [ print(a) for a in answer]
else:
    print(-1)