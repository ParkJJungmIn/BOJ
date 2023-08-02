from collections import deque
import sys

Y,X = map(int,input().split())
board = []
start = ()
end = ()
for y in range(Y):
    row = list(input())
    for x in range(X):
        if row[x] == 'M':
            start = (x,y)
        elif row[x] == 'Z':
            end = (x,y)
    board.append(row)

match_dict = { (-1,0) : ['2', '1', '+', '-'], 
                (1,0) : ['3','4', '+', '-'] , 
                (0,1) : ['2', '3', '+', '|'] , 
                (0,-1) : ['1','4','+','|']
}
# 1 r, 2 ㄴ 3 _| 4 ㄱ
change_dir = {
    '1' : { (0,-1) : (1,0) , (-1,0) : (0,1) }  ,
  '2' : { (-1,0) : (0,-1) , (0,1): (1,0) },
  '3' : { (0,1) : (-1,0), (1,0) : (0,-1)},
  '4' : { (1,0) : (0,1), (0,-1) : (-1,0) },
}

answer ={
    (1,1) : '1',
    (1,-1) : '2',
    (-1,-1) : '3',
    (-1,1) : '4'
}

def bfs( x,y, dir) :
    global miss_point

    q = deque()
    q.append( (x,y,dir) )
    check_list = []
    while q:
        now_x,now_y,dir = q.popleft()

        x = now_x + dir[0]
        y = now_y + dir[1]

        if 0<=x<X and 0<=y<Y and  board[y][x] in match_dict[dir] and board[y][x] != '.':
            
            if board[y][x] in ['|' , '-' , '+'] :
                q.append( (x,y,dir))
            else:
                next_dir = change_dir[ board[y][x] ][ dir ]
                q.append( (x,y,next_dir))

        elif 0<=x<X and 0<=y<Y  and board[y][x] == '.' and board[now_y][now_x] not in ['M','Z']:
            check_list.append( (now_x,now_y) )
            miss_point = (x,y)
            break
    return check_list

start_check = []
end_check = []
miss_point = ()
for move in match_dict.keys():
    start_check += bfs(start[0] , start[1], move)
    end_check += bfs(end[0] , end[1], move)

end_check = end if not end_check else end_check[0]
start_check = start if not start_check else start_check[0]

# 지워진 블록이 4면으로 연결되어 있는지 체크하기
cross_flag = True
for (tmp_x,tmp_y), tmp_match in match_dict.items():
    tmp_x += miss_point[0]
    tmp_y += miss_point[1]
    if not (0<=tmp_x<X and 0<=tmp_y<Y and board[tmp_y][tmp_x] in tmp_match):
        cross_flag = False

if cross_flag == True:
    print(miss_point[1]+1 , miss_point[0]+1, '+')
else:
    if end_check[0]==miss_point[0]==start_check[0]:
        print(miss_point[1]+1 , miss_point[0]+1, '|')
    elif end_check[1]==miss_point[1]==start_check[1]:
        print(miss_point[1]+1 , miss_point[0]+1, '-')
    else:
        ec_x, ec_y = end_check
        mp_x, mp_y = miss_point
        sc_x, sc_y = start_check

        tmp1 =(ec_x - mp_x, ec_y - mp_y)
        tmp2 =(sc_x - mp_x, sc_y - mp_y)

        tmp = tuple(sum(x) for x in zip(tmp1, tmp2))
        print(miss_point[1]+1, miss_point[0]+1, answer[tmp])