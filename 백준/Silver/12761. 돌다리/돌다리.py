A,B,N,M = map(int,input().split())
visited = [float('inf')] * 100001

from collections import deque
queue = deque([N])
visited[N] = 0

cal = [-A,-B,A,B,-1,1]

while queue:
    now = queue.popleft()
    now_visited = visited[now]

    if not 0<=now<=100000:
        continue
    
    for c in cal:
        c += now
        if 0<=c<=100000 and visited[c] > now_visited+1:
            visited[c] = now_visited + 1
            queue.append( c )
    
    for c in [A*now, B*now]:
        if 0<=c<=100000 and visited[c] > now_visited+1:
            visited[c] = now_visited + 1
            queue.append( c )


print(visited[M])