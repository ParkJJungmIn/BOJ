N,M = map(int,input().split())

board = [  list(map(int,input().split())) for _ in range(N)]

end_time , end_col, end_row  = map(int,input().split())

visited = [ [False] * M for _ in range(N)]

def bfs(stack):
    move = [(0,1), (1,0), (-1,0),(0,-1)]

    next_stack = set()
    for now_col, now_row in stack:
        for move_col, move_row in move:
            move_col += now_col
            move_row += now_row

            if 0<=move_col<N and 0<=move_row<N and visited[move_col][move_row] is False:
                if board[move_col][move_row] == 0:
                    board[move_col][move_row] = board[now_col][now_row]
                elif board[move_col][move_row] > board[now_col][now_row]:
                    board[move_col][move_row] = board[now_col][now_row]

                next_stack.add( (move_col, move_row) )

    for v_col, v_row in next_stack:
        visited[v_col][v_row] = True

    return list(next_stack)

stack = []

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            stack.append((i,j) )
            visited[i][j] = True

time = 0

while time != end_time:
    next_stack = bfs(stack)
    stack = next_stack
    time+=1

print(board[end_col-1][end_row-1])