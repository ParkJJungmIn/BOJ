import sys
input =sys.stdin.readline

N,M = map(int, input().split())

board = []
zero_set = set()
for y in range(N):
    row = list(map(int,list(input().strip() ) )) 
    for x,val in enumerate(row):
        if val == 0:
            zero_set.add( (x,y) )
    board.append( row )

move = [ (-1,0), (0,-1), (1,0), (0,1)] 

area = [ [0] * M for _ in range(N)]

def bfs( x,y ):
    global area_num

    visited = set()
    q = [(x,y)]
    while q :
        x,y = q.pop()
        for tmp_x, tmp_y in move:
            tmp_x += x
            tmp_y += y
            if 0<=tmp_x<M and 0<=tmp_y<N and board[tmp_y][tmp_x] == 0 and (tmp_x,tmp_y) not in visited:
                visited.add( (tmp_x,tmp_y) )
                q.append( (tmp_x,tmp_y) )
                area[tmp_y][tmp_x] = area_num

    
    cnt = len(visited)
    if cnt == 0 :
        board[y][x] = 1
        area[y][x] = area_num
    else:
        for (v_x,v_y) in visited:
            board[v_y][v_x] = cnt
    area_num += 1

# [ print(b) for b in board]

area_num = 1 
for y in range(N):
    for x, val in enumerate(board[y]):
        if (x,y) in zero_set and board[y][x] == 0:
            bfs(x,y)

for  y in range(N):
    tmp = []
    for x, val in enumerate(board[y]):
        if (x,y) not in zero_set :
            cnt = 1
            tmp_area = []
            for idx, (tmp_x,tmp_y) in enumerate(move):
                tmp_x += x
                tmp_y += y
                if (tmp_x,tmp_y) in zero_set: 
                    if area[tmp_y][tmp_x] not in tmp_area:
                        cnt += board[tmp_y][tmp_x]
                        tmp_area.append( area[tmp_y][tmp_x] )
            tmp.append(str(cnt%10))
        else:
            tmp.append('0')
    print( ''.join(tmp))