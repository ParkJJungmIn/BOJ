
N,M = map(int,input().split())

start, end = map(int,input().split())

from collections import defaultdict
from heapq import heappush, heappop
graph = defaultdict(list)

for _ in range(M):
    x,y,cost = map(int, input().split())
    graph[x].append( (y,cost) )
    graph[y].append( (x,cost) )

visited = [ 0 for _ in range(N+1)]

def dij():
    
    h = [(-float('inf'), start)]
    visited[start] = float('inf')

    while h:
        now_cost, now = heappop(h)
        now_cost *= (-1)

        if visited[now] > now_cost:
            continue

        for next, next_cost in graph[now] :
            next_cost = min(now_cost,next_cost)

            if visited[next] < next_cost:
                visited[next] = next_cost
                heappush(h,(-next_cost,next))
        
dij()
# print(graph)
print(visited[end])