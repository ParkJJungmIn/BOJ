from collections import deque
T = int(input())
for _ in range(T) : 
    N,K = map(int, input().split())
    bulid_speed = list(map(int, input().split()))

    graph = [ [] for _ in range(N)]
    indegree = [0] * (N)

    for i in range(K):
        start, end = map(int, input().split())
        start -= 1
        end -= 1

        graph[start].append(end)
        indegree[end] += 1

    W = int(input())
    
    def topological_sort():
        q = deque()
        costs = [ 0 for _ in range(N) ]

        for j in [ i for i in range(N) if indegree[i] == 0] :
            q.append(j)
            costs[j] = bulid_speed[j]


        while q:
            start = q.popleft()

            for next in graph[start]:
                indegree[next] -= 1

                if indegree[next] == 0 :
                    q.append(next)
                
                costs[next] = max(costs[next], costs[start] + bulid_speed[next])

                    
                    
        return costs[W-1]
                    
    print(topological_sort())