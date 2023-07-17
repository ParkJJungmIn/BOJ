from collections import deque
import sys

input = sys.stdin.readline

Y,X = map(int,input().split())

board = []
two_point = []

dot_q , dot_tmp, bfs_q, bfs_tmp = deque(),deque(),deque(),deque()

for y in range(Y):
    row = list(input())
    for x in range(X):
        if row[x] == 'L':
            two_point.append( [x,y] )
            dot_q.append( (x,y) )
            row[x] = '.'

        elif row[x] == '.':
            dot_q.append( (x,y) )
    board.append(row)

move = [ (0,1), (1,0), (-1,0) ,(0,-1)]
start, end = two_point[0], two_point[1]

answer = 0

dot_visited = [ [0] * X for _ in range(Y)]
bfs_visted = [ [0] * X for _ in range(Y)]

bfs_q.append( (start[0], start[1]) )
bfs_visted[start[1]][start[0]] = 1

while True:
    while dot_q:

        dot_x,dot_y = dot_q.popleft()
        if board[dot_y][dot_x] == 'X':
            board[dot_y][dot_x] = '.'

        for tmp_x, tmp_y in move:
            tmp_x += dot_x
            tmp_y += dot_y
            if 0 <= tmp_x < X and 0 <= tmp_y < Y and not dot_visited[tmp_y][tmp_x]:
                if board[tmp_y][tmp_x] == '.':
                    dot_q.append( (tmp_x,tmp_y) )
                else:
                    dot_tmp.append( (tmp_x,tmp_y) )

                dot_visited[tmp_y][tmp_x] = 1

    while bfs_q:
        bfs_x,bfs_y = bfs_q.popleft()
        if [bfs_x,bfs_y] == end:
            print(answer)
            exit()

        for tmp_x, tmp_y in move:
                tmp_x += bfs_x
                tmp_y += bfs_y
                if 0 <= tmp_x < X and 0 <= tmp_y < Y and not bfs_visted[tmp_y][tmp_x]:
                    if board[tmp_y][tmp_x] == '.':
                        bfs_q.append( (tmp_x,tmp_y) )
                    else:
                        bfs_tmp.append( (tmp_x,tmp_y) )

                    bfs_visted[tmp_y][tmp_x] = 1
    answer += 1
    bfs_q, dot_q = bfs_tmp, dot_tmp
    bfs_tmp, dot_tmp = deque(),deque()