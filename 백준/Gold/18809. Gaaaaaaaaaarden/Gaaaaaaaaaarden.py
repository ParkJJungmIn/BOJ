import sys
input = sys.stdin.readline

Y,X,G,R = map(int,input().split())

board= []
com = []
for y in range(Y):
    x = list(map(int,input().split()))
    com += [ (idx,y) for idx,tmp in enumerate(x) if tmp == 2]
    board += [x]


from itertools import combinations

com1 = list(combinations( com, G ))
com2 = list(combinations( com, R ))

def search( green, red ):
    tmp_board = [ [ 'N' for x in range(X)] for y in range(Y)]
    for x,y in green :
        tmp_board[y][x] = 'G'
    for x,y in red:
        tmp_board[y][x] = 'R'
    move = [ (0,1) , (1,0) , (0,-1), (-1,0)]
    count = 0

    now = green + red
    next = []

    while True:
        change = 0
        visited = set()
        for x,y in now:
            if tmp_board[y][x] in ['R','G'] and (x,y) not in visited:
                for tmpx , tmpy in move:
                    tmpx += x
                    tmpy += y
                    if 0<=tmpy<Y and 0<=tmpx<X and board[tmpy][tmpx] != 0:
                        if tmp_board[tmpy][tmpx] == 'N':
                            tmp_board[tmpy][tmpx] = tmp_board[y][x]
                            visited.add( (tmpx, tmpy) )
                            next.append( (tmpx,tmpy) )
                            change += 1
                        elif tmp_board[y][x] != tmp_board[tmpy][tmpx] and tmp_board[tmpy][tmpx] != 'F' and (tmpx,tmpy) in visited:
                            tmp_board[tmpy][tmpx] = 'F'
                            count += 1
        now = next
        next = []

        if change == 0:
            break


    # while True:
    #     change = 0
    #     visited = set()
    #     for y in range(Y):
    #         for x in range(X):
    #             if tmp_board[y][x] in ['R','G'] and (x,y) not in visited:
    #                 for tmpx , tmpy in move:
    #                     tmpx += x
    #                     tmpy += y
    #                     if 0<=tmpy<Y and 0<=tmpx<X and board[tmpy][tmpx] != 0:
    #                         if tmp_board[tmpy][tmpx] == 'N':
    #                             tmp_board[tmpy][tmpx] = tmp_board[y][x]
    #                             visited.add( (tmpx, tmpy) )
    #                             change += 1
    #                         elif tmp_board[y][x] != tmp_board[tmpy][tmpx] and tmp_board[tmpy][tmpx] != 'F' and (tmpx,tmpy) in visited:
    #                             tmp_board[tmpy][tmpx] = 'F'
    #                             count += 1
    #     if change == 0:
    #         break

    return count

tool = set()

answer = 0
for g in com1:
    for r in com2:
        [tool.add(gg) for gg in g]
        [tool.add(rr) for rr in r]
        if len(tool) == G+R :
            answer = max(answer,search(g,r))
        tool.clear()

print( answer)