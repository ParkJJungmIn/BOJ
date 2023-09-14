import sys
input = sys.stdin.readline

N = int(input())

node = [ [] for _ in range(N+1 )] 

for i in range(1,N+1):
    d = list(map(int,input().split()))

    k = d[0]
    point = 1
    while d[point] != -1:
        next_node = d[point]
        point += 1
        next_val = d[point]
        point += 1
        node[next_node].append((k,next_val)) 
        # node[k].add((next_node,next_val)) 

from collections import deque

distance = [0] * (N+1)
visited = [True] * (N+1) 

def bfs(start):
    q = deque()
    q.append( start )

    while q:
        now = q.pop()
        visited[now] = False

        for next, tmp_cost in node[now]:
            
            if visited[next]:
                visited[next] = False
                distance[next] = distance[now] + tmp_cost
                q.append( next )
bfs(1)
answer1 = max(distance)
next_start = distance.index(answer1)

distance = [0] * (N+1)
visited = [True] * (N+1) 

bfs(next_start)
answer2 = max(distance)

print( max(answer1,answer2))