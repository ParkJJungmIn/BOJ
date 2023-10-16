def place_queens(row, board, n):
    if row == n:
        return 1
    
    solutions = 0
    for col in range(n):
        if is_valid_placement(board, row, col, n):

            board[row] = col
            solutions += place_queens(row + 1, board, n)
            board[row] = -1
            
    return solutions

def is_valid_placement(board, row, col, n):
    for prev_row in range(row):
        if board[prev_row] == col or \
           board[prev_row] - prev_row == col - row or \
           board[prev_row] + prev_row == col + row:
            return False
    return True

n = int(input())

board = [-1] * n

print(place_queens(0, board, n))