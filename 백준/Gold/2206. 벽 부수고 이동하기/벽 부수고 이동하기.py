N,M = map(int,input().split())

board = [ list(map(int,list(input()))) for _ in range(N)]

visited = [ len(board[0]) * [float('inf')] for _ in range(N)]


from collections import deque
queue = deque([(0,0)])
visited[0][0] = 1
move = [ (0,1), (1,0), (-1,0), (0,-1)]
restart = []
while queue:
    now_x, now_y = queue.popleft()

    for tmp_x,tmp_y in move:
        tmp_x += now_x
        tmp_y += now_y

        if 0 <= tmp_x < N and 0 <= tmp_y < M:
            # 벽이 있을 경우
            if board[tmp_x][tmp_y] == 1:
                if visited[now_x][now_y]+1 < visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = visited[now_x][now_y]+1
                #     queue.append( (tmp_x,tmp_y) )
                    restart.append( (tmp_x, tmp_y) )
            else:
                if visited[now_x][now_y]+1 < visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = visited[now_x][now_y]+1
                    queue.append( (tmp_x,tmp_y) )


# [ print(v) for v in visited]
# print(restart)
for start in restart:
    queue = deque([start])
    move = [ (0,1), (1,0), (-1,0), (0,-1)]
    while queue:
        now_x, now_y = queue.popleft()

        for tmp_x,tmp_y in move:
            tmp_x += now_x
            tmp_y += now_y

            if 0 <= tmp_x < N and 0 <= tmp_y < M:
                if board[tmp_x][tmp_y] == 0 and visited[now_x][now_y]+1 < visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = visited[now_x][now_y]+1
                    queue.append( (tmp_x,tmp_y) )

print(-1 if visited[-1][-1] == float('inf') else visited[-1][-1] )