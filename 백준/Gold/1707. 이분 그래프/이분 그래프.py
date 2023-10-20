from collections import deque, defaultdict


N = int(input())

def bfs(start, graph, visited):
    q = deque()

    visited[start] = 1
    q.append(start)

    while q:
        now_start = q.popleft()
        now_visited = visited[now_start]

        for next in graph[now_start]:
            if visited[next] == 0:
                visited[next] = 3 - now_visited
                q.append(next)
            elif visited[next] == now_visited:
                return False
    return True
    

for _ in range(N):
    node_cnt, M = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (node_cnt+1)

    answer = True
    for i in range(1,node_cnt+1):
        if visited[i] == 0 and not bfs(i,graph, visited):
            answer = False
            break
    
    print( 'YES' if answer else 'NO')
