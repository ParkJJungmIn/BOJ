N = int(input())
boj = list(input())

from collections import deque
q = deque()

visited = [ float('inf') for _ in range(N)]

q.append((0,'O'))
visited[0] = 0

next = {
    'B' : 'O',
    'O' : 'J',
    'J' : 'B'
}

while q:
    start, next_char = q.popleft()
  
    steps = 1
    for idx in range(start+1,N):
        
        if boj[idx] == next_char:
            if visited[idx] == float('inf'):
                visited[idx] = (steps*steps) + visited[start]
                q.append( (idx, next[next_char]) )
            elif visited[idx] > visited[start] + (steps*steps) :
                visited[idx] = (steps*steps) + visited[start]
                q.append( (idx, next[next_char]) )
        steps += 1


print(-1 if visited[-1] == float('inf') else visited[-1] )