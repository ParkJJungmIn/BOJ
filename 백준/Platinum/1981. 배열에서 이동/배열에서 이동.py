import sys
from collections import deque
# input = sys.stdin.readline
def bfs(left,right):
    global visited, visited_key

    if board[0][0] < left or board[0][0] > right:
        return False

    queue = deque()
    queue.append( [0,0])
    visited_key += 1 
    flag = False
    while queue:
        x,y = queue.popleft()
        if (x,y) == (N-1,N-1):
            flag = True
            break

        for tmp_x, tmp_y in move:
            tmp_x += x
            tmp_y += y
            if 0<=tmp_x<N and 0<=tmp_y<N and visited[tmp_y][tmp_x] != visited_key:
                if left <= board[tmp_y][tmp_x] <= right:
                    queue.append( (tmp_x,tmp_y))
                    visited[tmp_y][tmp_x] = visited_key
    return flag

N = int(input())
board = []
num_line = set()

for _ in range(N):
    row = list(map(int,input().split()))
    board.append(row)
    [ num_line.add(r) for r in row]

num_line = sorted(list(num_line))
visited =  [ [0] * N for _ in range(N)]
visited_key = 0
move = [ (0,1),(0,-1),(1,0),(-1,0)]

left,right = (0,0)
answer = float('inf')

while left < len(num_line) and right < len(num_line):

    if bfs(num_line[left],num_line[right]):
        if left == right:
            print(0)
            exit()
        else:
            answer = min(answer, abs(num_line[right]-num_line[left]))
            left += 1
    else:
        right += 1

print(answer)