from collections import deque

N, M = map(str,input().split())

M = int(M)
num = list(N)
visited = set()
visited.add( (N,0) )
q = deque([ (num,0) ])
answer = 0

while q:
    tmp_num , cnt = q.pop()
    if cnt == M:
        answer = max(answer, int("".join(map(str, tmp_num)) ))
        continue

    for i in range( len(tmp_num) ):
        for j in range( len(tmp_num)):
            if (i == 0  and tmp_num[j] == '0') or (j == 0 and tmp_num[i] == '0') or i == j:
                continue

            tmp_num[i], tmp_num[j] = tmp_num[j], tmp_num[i]
            tmp_int = int("".join(map(str, tmp_num)) )
            if (tmp_int, cnt+1) not in visited:
                q.append( (tmp_num[:], cnt+1) )
                visited.add( (tmp_int, cnt+1)  )
            tmp_num[i], tmp_num[j] = tmp_num[j], tmp_num[i]

            tmp_num[j], tmp_num[i] = tmp_num[i], tmp_num[j]
            tmp_int = int("".join(map(str, tmp_num)) )
            if (tmp_int, cnt+1) not in visited:
                q.append( (tmp_num[:], cnt+1) )
                visited.add( (tmp_int, cnt+1) )
            tmp_num[j], tmp_num[i] = tmp_num[i], tmp_num[j]

print(-1 if answer == 0 else answer)