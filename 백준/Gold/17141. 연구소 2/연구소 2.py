N,M = map(int, input().split())


board = [  list(map(int,input().split())) for _ in range(N)]

start = []

for i in range(N):
    for idx,val in enumerate(board[i]):
        if val == 2:
            start.append( (i, idx) )


from collections import deque
import itertools
move = [ (0,1), (1,0) , (-1,0), (0,-1) ]
def bfs(visited, start):

    queue = deque(start)
    # print(visited)
    for s in start:
        visited[s[0]][s[1]] = 0

    max_answer = 0
    while queue:
        now_x,now_y = queue.popleft()
        now_count = visited[now_x][now_y]

        for next_x, next_y in move:
            next_x += now_x
            next_y += now_y
            if 0<=next_x<N and 0<=next_y<N and visited[next_x][next_y] == float('inf'):  
                visited[next_x][next_y] = 1+now_count         
                queue.append( (next_x,next_y) )
    visited = list(itertools.chain( *visited) )
    return max(visited) if float('inf') not in visited else float('inf')


start_com = list(itertools.combinations(start,M))

answer = float('inf')
for s in start_com:
    answer = min(answer,bfs([  [-1 if board[i][j] == 1 else float('inf') for j in range(N)] for i in range(N)] , s))

print( -1 if answer == float('inf') else answer)