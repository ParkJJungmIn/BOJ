X,Y = map(int, input().split())

N = int(input())
board = []
max_dict = {
    1 : 0,
    2 : X+Y+X,
    3 : X+Y+X+Y,
    4 : X
}

for _ in range(N+1):
    where , xy = map(int, input().split())
    if where in [1,4]:
        board.append( max_dict[where] + xy )
    else:
        board.append( max_dict[where] - xy )
    
answer = 0
total = (X+Y) * 2
for val in board:
    tmp = abs(board[-1]-val)
    tmp2 = total-tmp
    answer += min(tmp,tmp2)
print(answer)