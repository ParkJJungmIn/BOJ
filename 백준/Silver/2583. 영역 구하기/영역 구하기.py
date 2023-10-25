M,N,K = map(int, input().split() )
visited =set()

board = [ [0] * N for _ in range(M)]


for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    # print(x1,y1,x2,y2)
    for new_x in range(x1,x2):
        # print('x' , new_x)
        for new_y in range(M-y2,M-y1):
            # print('y' , new_y)
            board[new_y][new_x] = 1

move = [ (0,1) , (1,0), (0,-1), (-1,0)]
def bfs( x,y ):

    queue = [(x,y)]
    board[y][x] = 1  
    cnt = 1
    while queue:
        now_x,now_y = queue.pop()
        for next_x , next_y in move:
            next_x += now_x
            next_y += now_y

            if 0 <= next_x < N  and 0 <= next_y < M and board[next_y][next_x] == 0:
                board[next_y][next_x] = 1
                queue.append( (next_x,next_y) )
                cnt += 1

    return cnt

answer = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 0:
            answer.append ( bfs( x,y ) )
            
print(len(answer))
print(' '.join([ str(a) for  a in sorted(answer)]))