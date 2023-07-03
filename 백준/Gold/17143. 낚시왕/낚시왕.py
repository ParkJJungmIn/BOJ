from collections import defaultdict
import sys
input = sys.stdin.readline

Y,X,S = map(int, input().split())

board = [[ []for _ in range(X)] for _ in range(Y)]
shark = []
for s in range(S):
    y,x,speed,direct,weight = map(int,input().split())
    #인덱스, 스피드, 무게, 방향
    shark.append( [s,x-1,y-1, speed, weight, direct] )


now = 0
answer = 0
tmp = []
for now in range(X):
    for s_i,(idx,x,y,speed, weight, direct) in enumerate(shark):
        if now == x and not tmp:
            tmp= shark[s_i] + [s_i]
        elif now == x and tmp:
            if tmp[2] > y:
                tmp = shark[s_i] + [s_i]
    #상어 삭제하기
    if tmp:
        answer += shark[tmp[-1]][4]
        del shark[tmp[-1]]
    tmp = []

    move = {1:[0,-1], 2:[0,1], 3:[1,0],4:[-1,0]}
    change = [0,2,1,4,3]
    #상어 움직이기
    tmp_map = defaultdict(list)
    del_list = []
    for s_i, sha in enumerate(shark):
        s,x,y, speed, weight, direct = sha

        # 스피드계산
        tmp_x , tmp_y = x,y
        tmp_move = move[direct]

        while speed != 0:
            if 0<= x+tmp_move[0] < X and 0 <= y+tmp_move[1] < Y:
                x = x+tmp_move[0]
                y = y+tmp_move[1]
                speed -= 1
            else:
                direct = change[direct]
                tmp_move= move[direct]
        
        if len(tmp_map[(x,y)]) >= 1 :
            if tmp_map[(x,y)][0] > weight:
                del_list.append(s)
            else:
                del_list.append( tmp_map[(x,y)][1] )
                tmp_map[(x,y)] = [weight,s]
        else:
            tmp_map[(x,y)] = [weight,s]
    
            
        shark[s_i][1] = x
        shark[s_i][2] = y
        shark[s_i][5] = direct
    shark = [ s for s in shark if s[0] not in del_list]
print(answer)