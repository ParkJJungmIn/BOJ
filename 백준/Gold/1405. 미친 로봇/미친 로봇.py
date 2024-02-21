N, right, left, down, up = map(int,input().split())

move = [(0,1, right),(0,-1, left),(1,0, down),(-1,0, up)]

from collections import defaultdict

visited = defaultdict(lambda: False)
answer = 0.0

def dfs(count, pos, percent):
    global answer
    if N == count:
        answer += percent
        return
    
    visited[pos] = True

    for mx,my,per in move:
        if per == 0: continue
        
        next_pos = (pos[0]+mx, pos[1]+my)
        if visited[next_pos] == False:
            dfs( count+1, next_pos, percent * ( per/100 )  )
            visited[next_pos] = False

dfs(0,(0,0), 1)

print(answer)