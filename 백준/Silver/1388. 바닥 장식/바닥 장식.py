N, M = map(int,input().split())

board = [ list(input()) for _ in range(N)]

visited = [ [False] * M for _ in range(N)]

def bfs(col, row ):
    global visited

    stack = [ (col,row) ]
    shape = board[col][row]
    visited[col][row] = True
    move  = {
        '-' : [(0,-1),(0,1)],
        '|' : [(1,0),(-1,0)],
    }

    while stack:
        now_col , now_row = stack.pop()

        for next_col, next_row in move[shape]:
            next_col += now_col
            next_row += now_row

            if 0<=next_col<N and 0<=next_row<M and board[next_col][next_row] == shape \
                and not visited[next_col][next_row]:

                stack.append( (next_col, next_row) )
                visited[next_col][next_row] = True

answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] is False:
            bfs(i,j)
            answer += 1

print(answer)