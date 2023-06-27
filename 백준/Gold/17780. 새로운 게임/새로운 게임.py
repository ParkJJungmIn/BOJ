N,K = map(int, input().split())
board = [ list(map(int,input().split())) for _ in range(N) ]
k_board = [ [ [] for _ in range(N)] for _ in range(N)]
position = []

for k in range(K):
    y,x,move = map(int,input().split())
    position.append( [x-1,y-1,move] )
    k_board[y-1][x-1].append(k)

command = { 1: [1,0], 2:[-1,0],3:[0,-1], 4:[0,1]  }
change = [0,2,1,4,3]

for count in range(1,1001):
    for i in range(K):
        # print(position)
        x,y,move = position[i]
        if k_board[y][x][0] != i :
            continue
        
        trans = 1
        # 벽넘거나 마주친 곳이 2일 때,
        if not(0<=x + command[move][0]<N and 0<=y + command[move][1]<N) or board[y + command[move][1]][x + command[move][0]] == 2:
            position[i][2] = change[position[i][2] ]
            trans = -1

        move_x,move_y = x + (command[move][0] * trans) , y + (command[move][1] * trans)

        if 0<=move_x<N and 0<=move_y<N and board[move_y][move_x] != 2:
            
            for c in k_board[y][x] :
                    position[c][:2] = [move_x,move_y]

            if board[move_y][move_x] == 1:
                k_board[y][x] = k_board[y][x][-1::-1]
            
            k_board[move_y][move_x] += k_board[y][x]
            k_board[y][x] = []

            if len(k_board[move_y][move_x]) >= 4:
                print(count)
                exit()

print(-1)