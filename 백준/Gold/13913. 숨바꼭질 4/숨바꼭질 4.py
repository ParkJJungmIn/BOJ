N,M = map(int, input().split())

from collections import deque

visited = [-1] * 200001
visited[N] = 0

queue = deque()
queue.append( (N,0) )

last = ()

while queue:
    now, count = queue.popleft()

    if now == M:
        last = (now,count)
        break

    if now <= M:
        moves = [ now-1, now+1, now*2 ]
    else:
        moves = [ now-1 ]

    for m in moves:
        if 0 <= m <= 100000 and visited[m] == -1 :
            visited[m] = count+1
            queue.append( (m,count+1) )

answer = [last[0]]
tmp_now = last[0]
tmp_count = last[1]-1
while tmp_count != -1 :
    
    moves = [tmp_now-1, tmp_now+1]
    if tmp_now % 2 == 0:
        moves.append(tmp_now//2) 

    for m in moves:
        if visited[m] == tmp_count:
            answer.append(m)
            tmp_now = m
            break

    tmp_count -= 1
   
answer.reverse()
print(len(answer)-1)
print(*answer)