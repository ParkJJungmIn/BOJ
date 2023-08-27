N,M = map(int,input().split())

a_start = list(map(int,input().split()))
a_end = list(map(int,input().split()))

b_start = list(map(int,input().split()))
b_end = list(map(int,input().split()))


move = [(0,1), (1,0), (-1,0), (0,-1)]
from collections import deque

def bfs(start,end,root):
    
    queue = deque([start+[1]])
    visited = [ [-1] * (N+1 )for _ in range(M+1)]
    visited[start[1]][start[0]] = 0

    return_cnt = -1
    # print(queue)
    while queue:

        x,y,cnt = queue.popleft()
        
        if return_cnt != -1:
            break

        for tmp_x,tmp_y in move:
            tmp_x += x
            tmp_y += y
            
            if 0<=tmp_x<=N and 0<=tmp_y<=M and visited[tmp_y][tmp_x] == -1 and (tmp_x,tmp_y) not in root:
                queue.append( (tmp_x,tmp_y,cnt+1))
                visited[tmp_y][tmp_x] = cnt

                if [tmp_x,tmp_y] == end:
                    return_cnt = cnt
                    break 

    return (return_cnt,visited)

def find_root(cnt,visited,end):

    root = set()
    root.add( tuple(end) )
    cnt -= 1
    while cnt != -1:
        x,y = end

        for tmp_x, tmp_y in move:
            tmp_x += x
            tmp_y += y
            if 0<=tmp_x<=N and 0<=tmp_y<=M and visited[tmp_y][tmp_x] == cnt:
                end = (tmp_x,tmp_y)
                root.add( (tmp_x,tmp_y) )
                break
        cnt -= 1
    return root



a_cnt,a_visited = bfs(a_start,a_end,[tuple(b_start) , tuple(b_end)] )
b_cnt,b_visited = bfs(b_start,b_end,[tuple(a_start) , tuple(a_end)])

a_root = find_root(a_cnt,a_visited,a_end)
b_root = find_root(b_cnt,b_visited,b_end)

ab_cnt,a_visited = bfs(a_start,a_end,b_root)
ba_cnt,b_visited = bfs(b_start,b_end,a_root)


if  ab_cnt != -1 and ba_cnt != -1:
    print( min( ab_cnt+b_cnt , ba_cnt+a_cnt )  )
elif ab_cnt != -1 and ba_cnt == -1:
    print( ab_cnt+b_cnt  )
elif ab_cnt == -1 and ba_cnt != -1:
    print(  ba_cnt+a_cnt)
else:
    print('IMPOSSIBLE')