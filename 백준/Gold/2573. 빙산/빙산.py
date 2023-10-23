from collections import defaultdict, deque

X,Y = map(int,input().split())

# board = [ list(map(int,input().split())) for _ in range(X)]
board = []
checked = set()

for x in range(X):
    row = list(map(int,input().split()))
    board.append(row)
    for y_i,y_v in enumerate(row):
        if y_v != 0:
            checked.add( ( x,y_i ) )


move = [ (0,1), (1,0), (-1,0), (0,-1)]

def bfs( checked ):
    queue = deque( [list(checked)[0]] )
    visited =set()
  
    while queue:
        x,y = queue.pop()
        
        for tmp_x, tmp_y in move:
            tmp_x += x
            tmp_y += y
            
            if (tmp_x, tmp_y) in checked and (tmp_x, tmp_y) not in visited :
                visited.add( (tmp_x, tmp_y) )
                queue.appendleft( (tmp_x , tmp_y ))

    return len(checked) == len(visited)


answer = 0
while True:
    
    # True면 아직 하나로 뭉쳐있다라는 뜻
    if not bfs(checked):
        break


    count = defaultdict(int)
    remove = set()
    for tmp_x, tmp_y in list(checked):
        count[(tmp_x,tmp_y)] = board[tmp_x][tmp_y]

        for move_x, move_y in move:
            move_x += tmp_x
            move_y += tmp_y
            if 0<=move_x<X and 0<=move_y<Y and board[move_x][move_y] == 0 and count[(tmp_x,tmp_y)] > 0:
                count[(tmp_x,tmp_y)] -= 1
            

    for key,value in count.items() :
        if value == 0:
            remove.add( key )
        board[key[0]][key[1]] = value
    
    checked = checked-remove
    if not checked:
        answer = 0
        break
    answer += 1

print(answer)