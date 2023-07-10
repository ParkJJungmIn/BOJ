import sys
input = sys.stdin.readline

N = int(input())

from collections import deque
queue = deque([])

# queue = deque( list(map(int,input().split() ))  )
for _ in range(N):
    queue.append( int(input()) )


stack = []
answer = 0

for now in queue:
    # print(stack)
    if not stack:
        stack.append( [now,1] )
        continue
    else:

        while stack and stack[-1][0] < now:
            answer += stack.pop()[1]
        
        if not stack:
            stack.append( [now,1] )
            continue

        if stack[-1][0] == now :
            cnt = stack.pop()[1]
            answer += cnt

            if stack:
                answer += 1

            stack.append( [now, cnt+1] )
        else:
            stack.append([now,1])
            answer += 1

print(answer)