from collections import defaultdict, deque
N = int(input())
num_dict = defaultdict()
# num_index = defaultdict(list)

from math import ceil
def coord_to_index(coord):
    
    x,y = coord
    tmp_index = -1
    if x % 2 == 0 :
        tmp_index = N * (x-1) + ( ceil( (y-1) /2))
    else:
        tmp_index = N * (x-1) + ( ceil(y/2) ) 
    print(coord, tmp_index )
    return tmp_index

def index_to_coord(index):
    count = 0
    tmp_y = 0
    for i in range(N):
        current_row_columns = N - (i % 2)
        
        if count + current_row_columns >= index:
            tmp_y = i + 1
            break
        count += current_row_columns
    
    tmp_x = 2 if not tmp_y % 2 else 1

    for i in range(count+1,index):
        tmp_x += 2

    return ( (tmp_y, tmp_x), (tmp_y,tmp_x+1) )

# print( index_to_coord(5))
# print( coord_to_index( (2,9) ))

tmp_index = 1
for i in range(N):
    loop = N if i % 2 == 0 else N-1
    tmp_x = i+1
    tmp_y = 0 if i % 2 == 0 else 1

    for j in range(loop):
        a,b = map(int, input().split())
        tmp_y += 1
        num_dict[(tmp_x,tmp_y)] = (a,tmp_index)
        tmp_y += 1
        num_dict[(tmp_x,tmp_y)] = (b,tmp_index)
        tmp_index += 1


visited =  [ -1 for _ in  range( (N*N-N//2)+1 )]
queue = deque()
queue.append(1)
visited[1] = 1
move = [ (1,0) , (0,1) , (-1,0), (0,-1)]

flag = True
while flag and queue:
    now = queue.popleft()
    start_list = index_to_coord(now)
    for x, y in start_list:
        for tmp_x,tmp_y in move:
            tmp_x += x
            tmp_y += y
            if (tmp_x,tmp_y) in num_dict and num_dict[(tmp_x,tmp_y)][0] == num_dict[(x,y)][0] :
                tmp_index = num_dict[(tmp_x,tmp_y)][1]
                if visited[tmp_index] == -1:
                    visited[tmp_index] = now
                    queue.append(tmp_index)
last_index = 0
for i in range( len(visited)-1 ,-1,-1):
    if visited[i] != -1:
        last_index = i
        break

answer = [last_index]

while last_index != 1:
    answer.append(visited[last_index])
    last_index = visited[last_index]

answer.reverse()
print(len(answer))
print(*answer)