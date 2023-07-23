from collections import deque
import sys


Y,X = map(int,input().split())

board = [ list(input()) for _ in range(Y)]

N = int(input())

hits = list(map(int,input().split()))

move = [ (0,1), (1,0), (-1,0), (0,-1)]

def bfs(start):

    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x,y = queue.popleft()
        
        for tmp_x, tmp_y in move:
            tmp_x += x 
            tmp_y += y
            if 0 <= tmp_x < X and 0 <= tmp_y < Y and board[tmp_y][tmp_x] == 'x' and not (tmp_x,tmp_y) in visited:
                queue.append( (tmp_x, tmp_y))
                visited.add( (tmp_x,tmp_y))
    return visited


def mineral(height, side):

    remove = [ i for i in range(X) if board[height][i] == 'x']

    if len(remove) == 0:
        return
    elif side == 'right':
        remove = remove[0]
    else:
        remove = remove[-1]
    
    board[height][remove] = '.'
    visited = set()
    
    # 밑바닥의 미네랄 쭉 타기

    for x in range(X):
        if board[Y-1][x] == 'x' and not (x,Y-1) in visited:
            visited |=  bfs( (x,Y-1) ) 
    for tmp_x, tmp_y in move:
        tmp_x += remove
        tmp_y += height
        if 0 <= tmp_x < X and 0 <= tmp_y < Y and board[tmp_y][tmp_x] == 'x' and not (tmp_x,tmp_y) in visited:
            tmp_visited = bfs( (tmp_x,tmp_y) )
            start = 0
            flag = True
            while flag:
                start += 1
                for set_x, set_y in tmp_visited:
                    set_y += start

                    if (0 <= set_y < Y and board[set_y][set_x] == '.') or (set_x, set_y) in tmp_visited:
                        continue
                    else:
                        start -= 1
                        flag = False
                        break
            
            if start > 0 :
                for set_x, set_y in tmp_visited:
                    board[set_y][set_x] = '.'
                for set_x, set_y in tmp_visited:
                    board[set_y+start][set_x] = 'x'
                    


for idx, h  in enumerate(hits):
    
    if idx % 2 == 0:
        mineral(Y-h,'right')
    else:
        mineral(Y-h,'left')

for b in board:
    print(''.join(b))