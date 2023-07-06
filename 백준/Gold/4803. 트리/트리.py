import sys
input = sys.stdin.readline

case_n = 1

while True:

    N,M = map(int,input().split())
    if (N,M) == (0,0):
        break

    graph = [ [0] * (N+1) for n in range(N+1)]

    for _ in range(M):
        a,b = map(int,input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    visited = [ 0 for _ in range(N+1)]

    from collections import deque

    count = 0
    for n in range(1,N+1):

        if visited[n] == 1:
            continue

        queue = deque()
        queue.append(n)
        
        flag = True
        while queue:
            node = queue.popleft()
            if visited[node] == 1 :
                flag = False
                continue

            visited[node] = 1

            for i,v in enumerate(graph[node]):
                if v == 1 and not visited[i]:
                    queue.append(i)

        if flag:
            count += 1

    if count == 0:
        print(f'Case {case_n}: No trees.')
    elif count == 1:
        print(f'Case {case_n}: There is one tree.')
    else:
        print(f'Case {case_n}: A forest of {count} trees.')
    
    case_n += 1