from collections import deque

# 입력 받기
n, k = map(int, input().split())

q = deque([  i for i in range(1, n+1)])

answer = []

while q:
    for _ in range(k-1):
        q.append( q.popleft() )
    answer.append(str(q.popleft()))

print( '<' + ', '.join(answer) + '>')