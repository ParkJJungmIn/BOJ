import sys
input = sys.stdin.readline

from collections import deque

while True:
    Z,Y,X = map(int,input().split())
    if (Z,Y,X) == (0,0,0):
        break

    building = []
    start = []
    end = []
    for z in range(Z):
        tmp_y = []
        for y in range(Y):
            tmp_x = list(input())

            if 'S' in tmp_x:
                start = [ tmp_x.index('S'), y, z ]
            elif 'E' in tmp_x:
                end = [ tmp_x.index('E'), y, z ]
            
            tmp_y.append( tmp_x )
        building.append( tmp_y )
        input()
    queue = deque([])

    visited = [ [ [ 0 for _ in range(X) ] for _ in range(Y) ] for _ in range(Z) ]
    visited[start[2]][start[1]][start[0]] = 0
    queue.append(start)

    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):

            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            tmp_z = z + dz[i]

            if 0<=tmp_z<Z and 0<=tmp_x<X and 0<=tmp_y<Y and building[tmp_z][tmp_y][tmp_x] != '#':
                if visited[tmp_z][tmp_y][tmp_x] == 0:
                    visited[tmp_z][tmp_y][tmp_x] = visited[z][y][x] + 1
                    queue.append( (tmp_x, tmp_y, tmp_z))

    if visited[end[2]][end[1]][end[0]] != 0 :
        print( f"Escaped in {visited[end[2]][end[1]][end[0]]} minute(s).")
    else:
        print('Trapped!')