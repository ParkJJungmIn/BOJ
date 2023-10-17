N = int(input())


board = [ list(map(int,input().split() )) for _ in range(N)]

def check_color(x,y,size):
    now = board[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != now:
                return None
    
    return now


def colorbook(x,y,size):
    color = check_color(x,y,size)

    if color is not None:
        return [0,1] if color == 1 else [1,0]
    

    half = size // 2

    left = colorbook(x,y, half)
    right = colorbook(x+half,y, half)
    down_left = colorbook(x,y+half, half)
    down_right = colorbook(x+half,y+half, half)

    return [  sum(i) for i in list(zip(left, right, down_left, down_right)) ]

answer = colorbook(0,0,N)

print(answer[0])
print(answer[1])