N,M = map(int, input().split())

graph= [ [] for _ in range(N+1)]
order = [0] * (N+1) 

for i in range(M):
    a,b = map(int, input().split())

    order[b] += 1
    graph[a].append(b)

from collections import deque

queue = deque([ i for i in range(1,N+1) if order[i] == 0])

answer = []
while queue:
    now = queue.popleft()
    answer.append(str(now))
    for node in graph[now]:
        order[node] -= 1
        
        if order[node] == 0:
            queue.appendleft(node)

    
print(' '.join(answer))