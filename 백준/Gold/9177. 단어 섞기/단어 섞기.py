N = int(input())
from collections import deque

for i in range(1,N+1):
    a,b,c = map(list,input().split())
    q = deque()

    visited = set()

    q.append( (0,0,0) )

    answer = "no"

    while q:
        now_a, now_b, now_c = q.pop()

        if now_c == len(c):
            answer = "yes"
            break

        if now_a < len(a) and a[now_a] == c[now_c] and (now_a+1, now_b, now_c+1) not in visited:
            q.appendleft( (now_a+1, now_b, now_c+1) )
            visited.add( (now_a+1, now_b, now_c+1) ) 

        if now_b < len(b) and b[now_b] == c[now_c] and (now_a, now_b+1, now_c+1)  not in visited:
            q.appendleft( (now_a, now_b+1, now_c+1) )
            visited.add( (now_a, now_b+1, now_c+1) )

    print(f"Data set {i}: {answer}")