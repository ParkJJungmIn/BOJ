N,M = map(int,input().split())
from collections import deque, defaultdict

board = []

start = ()
water = ()
water_list = []
for i in range(N):
    tmp = list(input())
    board.append(tmp)

    if '*' in tmp:
        water_list.append( (i,tmp.index('*')) )
        
    if 'S' in tmp:
        start = ( i, tmp.index('S'))

move = [(0,1), (1,0), (-1,0) , (0,-1)]
def bfs( start ):
    global water_list

    q = deque()
    q.append(start)
    cnt = 0
    while q:
        tmp_water = []
        for w in water_list:
            for w_x, w_y in move:
                w_x += w[0]
                w_y += w[1]
                # print(w_x,w_y, N, M)
                if 0<=w_x<N and 0<=w_y<M and board[w_x][w_y] == '.':
                    tmp_water.append( (w_x, w_y) )
                    board[w_x][w_y] = '*'
        water_list = tmp_water

        tmp_q = []
        while q:
            now_x, now_y = q.pop()
        
            for next_x,next_y in move:
                next_x += now_x
                next_y += now_y
        
                if 0<=next_x<N and 0<=next_y<M:
                    if board[next_x][next_y] == 'D':
                        return cnt+1
                    if board[next_x][next_y] == '.':
                        tmp_q.append( (next_x, next_y) )
                        board[next_x][next_y] = 'S'

        q = tmp_q
        cnt+=1
    return False
    
answer = bfs(start)
print(answer if answer else 'KAKTUS')