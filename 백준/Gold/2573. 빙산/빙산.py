Y,X = map(int, input().split())

board = []
checked = []

for y in range(Y):
    tmp = list(map(int,input().split() ))
    checked += [ (x,y) for x,i in enumerate(tmp) if i > 0]
    board.append( tmp )

from collections import deque

def bfs( x,y ):

    stack = deque([ (x,y) ])
    visited[y][x] = 1
    after = []
    while stack:
        tmpX, tmpY = stack.popleft()
        point = 0
        for m_x, m_y in move:
            m_x += tmpX
            m_y += tmpY

            if 0 <= m_x < X and 0 <= m_y < Y:
                if board[m_y][m_x] == 0:
                    point += 1
                elif not visited[m_y][m_x] and board[m_y][m_x]:
                    stack.append( (m_x,m_y) )
                    visited[m_y][m_x] = 1

        if point > 0 :
            after.append( (tmpX,tmpY,point) )

    for ax, ay, point in after :
        board[ay][ax] = max(0,board[ay][ax]-point )

    return 1


move = [ (0,1) , (1,0) , (-1,0), (0,-1)]

year = 0
while checked: 
    visited = [ [0] * X for _ in range(Y)]
    delete = []
    count = 0
    for c_x, c_y in checked:
        if  board[c_y][c_x] and not visited[c_y][c_x] :
            count += bfs(c_x,c_y)
        if not board[c_y][c_x]:
            delete.append( (c_x,c_y) )
    
    if count >= 2:
        print(year)
        exit(0)
    year += 1
    checked = sorted(list(set(checked) - set(delete)))

print(0)