N = int(input())

board = [  list( map(int,list(input()) ))  for _ in range(N)]

def check_bit(x,y,size):

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != board[x][y]:
                return False
    
    return board[x][y]

def divide(x,y,size):
    global one,two,three,four
    text = ''
    bit = check_bit(x,y,size)

    if bit is not False:
        return str(board[x][y])

    if size <= 1:
        # qurt.append( ((size ,board[x][y]))  )
        return str(board[x][y])

    half = size // 2

    text += divide(x,y, half)
    text += divide(x,y+half, half)
    text += divide(x+half,y, half)
    text += divide(x+half,y+half, half)

    return f"({text})"


answer = divide(0,0,N)

print(answer)