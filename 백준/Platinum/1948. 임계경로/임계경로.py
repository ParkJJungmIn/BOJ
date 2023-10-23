from collections import defaultdict, deque

N = int(input())
M = int(input())

from collections import defaultdict
first_graph = defaultdict(list)

for i in range(M):
    a,b,cost = map(int, input().split())
    first_graph[a].append( (b,cost))

start_degree = [0] * (N+1)


for g_list in first_graph.values():
    for g_val in g_list:
        start_degree[g_val[0]] += 1

start_index, end_index = map(int,input().split())
h = deque([start_index])

answer = float('inf')
cost_visited = [0] * (N+1)
cnt = defaultdict(list) 

while h:
    now_index = h.popleft()

    for  next_index, next_cost in first_graph[now_index]:
        start_degree[next_index] -= 1
        if cost_visited[next_index] < next_cost + cost_visited[now_index]:
            cost_visited[next_index] = next_cost + cost_visited[now_index]
            cnt[next_index] = [now_index]

        elif cost_visited[next_index] == next_cost + cost_visited[now_index]:
            cnt[next_index].append(now_index)

        if start_degree[next_index] == 0:
           h.append( next_index )


route_queue = deque([end_index])
visited = set()
while route_queue:
    now = route_queue.pop()
    
    for next in cnt[now]:
        if (now,next) not in visited:
            visited.add( (now,next) )
            route_queue.append(next)


print(cost_visited[end_index])
print(len(visited))