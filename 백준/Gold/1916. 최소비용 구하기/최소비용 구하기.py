import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append( (cost,b) )

start,end = map(int,input().split())

visited = [float('inf')] * (N+1)
visited[start] = 0

from heapq import heappop, heappush

h = []

heappush(h, (0,start) )

count = 1
while h:
    cost, now = heappop(h)
    
    if visited[now] < cost:
        continue

    for tmp_cost, next in graph[now]:
        tmp_cost += cost

        if visited[next] > tmp_cost:
            if visited[next] == float('inf'):
                count += 1
            visited[next] = tmp_cost
            heappush( h, (tmp_cost, next) )

            if count == len(visited)+1:
                break
            
            

print(visited[end])