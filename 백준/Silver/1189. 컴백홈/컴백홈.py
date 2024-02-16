R,C,K = map(int, input().split())

board = [ list(input()) for _ in range(R)]

visited = [ [False] * C for _ in range(R)]


move = [ (0,1), (1,0), (-1, 0), (0,-1)]
def dfs(visited , startX, startY, count):
    
    if count == K and (C-1, 0) == (startX, startY):
        return 1
    elif count > K:
        return 0

    result = 0    
    
    for mX, mY in move:
        mX += startX
        mY += startY
        if 0 <= mX < C and 0 <= mY < R and visited[mY][mX] is False and board[mY][mX] != 'T' :
            visited[mY][mX] = True
            result += dfs(visited, mX, mY, count+1)
            visited[mY][mX] = False
    
    return result

visited[-1][0] = True
print(dfs(visited, 0, R-1, 1))