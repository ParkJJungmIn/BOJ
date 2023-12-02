from collections import deque

def solution(land):
    answer = 0
    
    visited = [ [False] * len(land[0]) for y in range(len(land))]

    move = [ (0,1), (1,0) , (-1,0) , (0,-1)]

    oil_map = [ 0 for y in range(len(land[0]))]

    def bfs(x,y):
        
        queue = deque()
        queue.append( (x,y) )
        visited_set = set()
        visited_y = set()

        visited_set.add( (x,y) )
        visited_y.add( (y) )
        visited[x][y] = True

        while queue:
            now_x,now_y = queue.popleft()

            for m_x,m_y in move:
                m_x += now_x
                m_y += now_y

                if 0<=m_x<len(land) and 0<=m_y<len(land[0]) and not visited[m_x][m_y] and land[m_x][m_y] == 1:
                    queue.append((m_x,m_y) )
                    visited_set.add( (m_x, m_y) )
                    visited_y.add( (m_y) )
                    visited[m_x][m_y] = True

        cnt = len(visited_set)
        for y in visited_y:
            oil_map[y] += cnt


    for x in range(len(land)):
        for y in range( len(land[0]) ):
            if  not visited[x][y] and land[x][y] == 1:
                bfs(x,y)

    answer = max(oil_map)
    print(answer)
    return answer