board = [ list(input()) for i in range(5)]
move = [ (0,1) , (1,0), (-1,0), (0,-1)]

result = set()
def dfs( visited, depth, Y, S):
    
    if Y > 3:
        return

    if depth == 6:
        visited = sorted(visited)
        result.add(tuple(visited))
        return
    
    add_node = []
    for node in visited:
        for x,y in move:
            x += node[0]
            y += node[1]
            if not (x,y) in add_node and not (x,y) in visited and 0<=x<5 and 0<=y<5:
                add_node.append((x,y))

    for node in add_node:
        if board[node[0]][node[1]] == 'Y':
            dfs(visited+[node],depth+1, Y+1, S )
        else:
            dfs(visited+[node], depth+1, Y,S+1)

for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            dfs([(i,j)],0,0,1)

print(len(result))