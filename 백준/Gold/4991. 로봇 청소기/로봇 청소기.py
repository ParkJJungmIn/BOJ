from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline
move = [ (0,1),(1,0),(-1,0),(0,-1)]
def bfs(start):

    queue = deque()
    queue.append(start)
    
    visited = [ [0] * X for _ in range(Y)]
    # visited[start[1]][start[0]] = 1

    while queue:
        x,y = queue.popleft()

        for tmp_x, tmp_y in move:
            tmp_x += x
            tmp_y += y 

            if 0<=tmp_x<X and 0<=tmp_y<Y and not visited[tmp_y][tmp_x] and board[tmp_y][tmp_x] != 'x' :
                queue.append( [tmp_x,tmp_y] )
                visited[tmp_y][tmp_x] = visited[y][x] + 1

    return visited
    
while True:
    X,Y = map(int,input().split())
    if (X,Y) == (0,0):
        break

    board = []
    now = []
    checked = []

    answer = float('inf')

    for y in range(Y):
        tmp_x = list(input())
        for x,v in enumerate(tmp_x):
            if v == 'o' :
                now = [x,y]
            elif v == '*':
                checked.append([x,y])
        board.append(tmp_x)

    visited = bfs(now)
    first_checked = [0] * len(checked)

    for i, (ch_x, ch_y )in enumerate(checked):
        first_checked[i] = visited[ch_y][ch_x]
    
    if 0 in first_checked :
        print(-1)
        continue

    graph = [  [0 for _ in range(len(checked)) ]for _ in range( len(checked) )]

    for node_a in range( len(checked)-1 ):
        visited = bfs( checked[node_a] )

        for node_b in range( node_a+1, len(checked) ):
            check_x, check_y = checked[node_b]
            graph[node_a][node_b] = visited[check_y][check_x]
            graph[node_b][node_a] = graph[node_a][node_b]


    for per in permutations( range( len(checked) ) ):
        tmp_answer = first_checked[ per[0] ]
        start = per[0]

        for next_i in range(1,len(per) ):
            next = per[next_i]
            tmp_answer += graph[start][next]
            start = next

        answer = min(tmp_answer, answer)

    print(answer)