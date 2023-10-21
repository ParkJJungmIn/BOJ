from collections import deque

N = int(input())

board = [ list(input()) for _ in range(N)]
move = [(0,1), (1,0) , (-1,0) , (0, -1)]
def bfs(x,y):
    q = deque()
    visited = set()
    block = []

    q.append( (x,y) )
    visited.add( (x,y))

    while q :
        now_x, now_y = q.popleft()

        for next_x, next_y in move:
            next_x += now_x
            next_y += now_y

            if 0<=next_x<N and 0<=next_y<N:
                if board[next_x][next_y] == '0' and (next_x, next_y) not in block:
                    block.append( (next_x, next_y) ) 
                if board[next_x][next_y] == '1'  and (next_x, next_y) not in visited :
                    visited.add( (next_x, next_y) )
                    q.append( (next_x,next_y) )

                    if (next_x,next_y) == (N-1,N-1):
                        return True
                    
    for b_x,b_y in block:
        board[b_x][b_y] = '1'

    return False

answer = 0
while True:
    if bfs(0,0):
        break
    else:
        answer+=1

print(answer)