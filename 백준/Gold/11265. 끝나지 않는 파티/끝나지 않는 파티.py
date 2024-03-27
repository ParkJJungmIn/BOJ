N,M = map(int, input().split())

board = [  list(map(int,input().split())) for _ in range(N)]

for a in range(N):
    for b in range(N):
        for c in range(N):
            if board[b][c] > board[b][a] + board[a][c]:
                board[b][c] = board[b][a] + board[a][c]

for _ in range(M):
    a,b,time = map(int,input().split())

    if board[a-1][b-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')