N = int(input())

board = []
point = []
for y in range(N):
    row = list(input())

    for x in range(N):
        if row[x] == '#':
            point.append( (x,y) )
    board.append(row)
from collections import deque
q = deque()

start, end = point[0], point[1]

move = [ (0,1) , (0,-1), (1,0), (-1,0) ]

for i in range(4):
    q.append( (start[0],start[1],0,i) )

while q:
    x,y,cnt,dir = q.popleft()

    mx,my = move[dir]

    while True:
        x += mx
        y += my

        if 0<=x<N and 0<=y<N and board[y][x] != '*':
            if board[y][x] == '!':
                if dir in [0,1]:
                    q.append( (x,y,cnt+1,2) )
                    q.append( (x,y,cnt+1,3) )
                else:
                    q.append( (x,y,cnt+1,0) )
                    q.append( (x,y,cnt+1,1) )
            elif (x,y) == end:
                print(cnt)
                exit()
        else:
            break