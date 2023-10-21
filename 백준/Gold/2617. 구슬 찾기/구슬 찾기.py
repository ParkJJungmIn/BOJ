N,M = map(int,input().split())

from collections import defaultdict, deque

min_board = defaultdict(list)
max_board = defaultdict(list)

min_visited = [0] * (N+1)
max_visited = [0] * (N+1)

pivot = (N+1) // 2

for _ in range(M):
    a,b = map(int, input().split())

    min_board[b].append(a)
    max_board[a].append(b)

def bfs(start,board):

    visited = [0] * (N+1)
 
    q = deque()
    q.append(start)
    visited[start] = 1

    cnt = 0
    while q:
        now = q.popleft()

        for next in board[now]:
            if visited[next] == 0:
                cnt += 1
                q.append(next)
                visited[next] = 1
                
    if cnt >= pivot:
        return 1
    else:
        return 0

answer = 0

for i in range(1,N+1):
    answer += bfs(i, min_board)
    answer += bfs(i, max_board)

print(answer)