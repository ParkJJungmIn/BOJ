N = int(input())

board = [ list(map(int,input().split()) ) for _ in range(N)]

def find_xy(x1,y1,x2,y2):
    tmp_visited = set()
    for tmp_x in range(x1,x2):
        tmp_visited.add( (tmp_x, y1) )
    for tmp_y in range(y1,y2):
        tmp_visited.add( (x2,tmp_y))
    for tmp_x in range(x2,x1,-1):
        tmp_visited.add( (tmp_x,y2) )
    for tmp_y in range(y2,y1,-1):
        tmp_visited.add( (x1,tmp_y) )

    return tmp_visited


def find(a):
    if visited[a] != a :
        visited[a] = find(visited[a])
    
    return visited[a]

def union_find(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            visited[a] = b
        else:
            visited[b] = a

xy_list = [0]+ [ find_xy(x1,y1,x2,y2) for (x1,y1,x2,y2) in board]
visited = [ i for i in range(N+1)]

add_zero = 0
for i in range(1,N+1):
    if (0,0) in xy_list[i]:
        add_zero = 1

    for j in range(1,N+1):
        if i == j : continue

        if xy_list[i] & xy_list[j]:
            union_find(i,j)
for i in range(1,N+1):
    find(i)

print( len(set(visited[1:])) - add_zero )