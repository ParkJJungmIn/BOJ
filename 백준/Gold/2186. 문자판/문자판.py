M,N,K = map(int,input().split())

board = [ list(input()) for _ in range(M)]
answer = list(input())
memo = [ [ [-1] * len(answer) for _ in range(N) ] for _ in range(M)]

start = []
for y in range(M):
    for x in range(N):
        if board[y][x] == answer[0]:
            start.append( (x,y) )
cnt = 0
move = [(0,1),(1,0),(0,-1), (-1,0)]

def dfs(x,y,depth):
    if depth == len(answer):
        return 1
    if memo[y][x][depth] != -1:
        return memo[y][x][depth]

    memo[y][x][depth] = 0

    for tmp in range(4):
        for i in range(1,K+1):
            tmp_x,tmp_y = move[tmp]
            tmp_x = (tmp_x * i) + x
            tmp_y = (tmp_y * i) + y

            if 0<=tmp_x<N and 0<=tmp_y<M and board[tmp_y][tmp_x] == answer[depth]:
                memo[y][x][depth] += dfs(tmp_x,tmp_y,depth+1)
    
    return memo[y][x][depth]

for x,y in start:
    cnt += dfs(x,y,1)

print(cnt)