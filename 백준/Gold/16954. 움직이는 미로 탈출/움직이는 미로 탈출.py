def bfs( now_set , block_set ):
    tmp_set = set()
    for (x,y) in now_set:
        if (x,y) not in block_set:
            for tmp_x, tmp_y in move:
                tmp_x += x
                tmp_y += y
                if 0<=tmp_x<8 and 0<=tmp_y<8 and (tmp_x,tmp_y) not in tmp_set and (tmp_x,tmp_y) not in block_set:
                    if (tmp_x,tmp_y) == end:
                        print(1)
                        exit()
                    tmp_set.add( (tmp_x,tmp_y) )
    
    return tmp_set

def move_block(block_set):
    block_set = list(block_set)
    tmp_set = set()
    for idx,(b_x,b_y) in enumerate(block_set):
        if b_y + 1 < 8:
            tmp_set.add( (b_x,b_y+1))
    return tmp_set


N = 8
block_set = set()
for y in range(8):
    row = list(input())
    for x,val in enumerate(row):
        if val == '#':
            block_set.add( (x,y) )

move = [ (0,-1), (1,0), (0,1), (-1,0), (-1,1) , (1,1) , (1,-1),(-1,-1), (0,0)]

start = (0,7)
end = (7,0)

from collections import deque
now_set= set()
now_set.add( start )

while now_set :
    now_set = bfs(now_set,block_set)
    block_set = move_block(block_set)

print(0)