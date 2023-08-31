N,M = map(int,input().split())

board = [  list(map(int,input().split())) for _ in range(N)]

visited = [ [0] * M for _ in range(N)]
move = [(0,1),(1,0),(-1,0),(0,-1)]

cache = [[-1 for _ in range(M)] for _ in range(N)]

visited[0][0] = 1
answer = 0

def dfs(x, y, visited, cache):
    if (x, y) == (M-1, N-1):
        return 1
    
    if cache[y][x] != -1:
        return cache[y][x]
    
    answer = 0
    for tmp_x, tmp_y in move:
        next_x = tmp_x + x
        next_y = tmp_y + y

        if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x]:
            if board[y][x] > board[next_y][next_x]:
                visited[next_y][next_x] = 1
                answer += dfs(next_x, next_y, visited, cache)
                visited[next_y][next_x] = 0

    cache[y][x] = answer
    return answer

answer = dfs(0,0,visited,cache)
print(answer)