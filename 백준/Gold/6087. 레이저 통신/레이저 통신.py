from collections import deque
from heapq import heappop,heappush
import sys

input = sys.stdin.readline

X,Y = map(int,input().split())

two_point = []
board = []
for y in range(Y):

    row = list( input() )
    for x,v in enumerate(row):
        if v == 'C':
            two_point.append( (x,y) )
    board.append(row)

start,end = two_point

move = [ 0, [1,0], [-1,0], [0,1], [0,-1] ] # 북,남,동,서
mirror = [ 0, [1,3,4], [2,3,4], [1,2,3], [1,2,4]]

def bfs(start):
    start_x, start_y = start
    queue = []
    visited = [ [float('inf')] * X for _ in range(Y)]
    visited[start_y][start_x] = 0

    for i in range(1,5):
        heappush( queue, (0,i,start_x,start_y )  )
    
    while queue:
        mir_cnt, dir, x, y = heappop(queue)
        
        if (x,y) == end:
            print(mir_cnt)
            # [ print(v) for v in visited]
            exit()
        for m in mirror[dir]:

            tmp_x , tmp_y = move[m]

            tmp_x += x
            tmp_y += y 
            if 0 <= tmp_x < X and 0 <= tmp_y < Y and board[tmp_y][tmp_x] != '*' and visited[tmp_y][tmp_x] >= mir_cnt:
                # 일직선
                if dir == m  and visited[tmp_y][tmp_x] > mir_cnt:
                    heappush(queue,( mir_cnt, m,tmp_x, tmp_y)  )
                    visited[tmp_y][tmp_x] = mir_cnt
                elif dir == m  and visited[tmp_y][tmp_x] == mir_cnt:
                    heappush(queue,( mir_cnt, m,tmp_x, tmp_y)  )
                    visited[tmp_y][tmp_x] = mir_cnt-1
                elif dir != m and visited[tmp_y][tmp_x] >= mir_cnt+1:
                    heappush(queue,( mir_cnt+1, m ,tmp_x, tmp_y)  )
                    visited[tmp_y][tmp_x] = mir_cnt+1
bfs( start )