import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K, M = map(int, input().split())
end = []
start = deque([])
nums = defaultdict(set)
# nums = {i: set() for i in range(1, N + 1)}
board = []

if (1,1,1) == (N,K,M):
    print(1)
    exit()

for m in range(M):
    h = list(map(int, input().split()))
    if N in h:
        end.append(m)
    if 1 in h:
        start.append(m)
    for hh in h:
        nums[hh].add(m)
    board.append(h)

visited = [False] * M

def bfs(start_index, visited):
    queue = deque([(start_index, 1)])
    
    while queue:
        now, steps = queue.popleft()
        
        if now in end:
            return steps+1
        
        for b in board[now]:

            for check in nums[b]:
                if not visited[check]:
                    queue.append((check, steps + 1))
                    visited[check] = True

    return float('inf')

try:
    answer = [bfs(s, visited.copy()) for s in start]
    answer = min(answer)
except ValueError:
    print(-1)
    exit()

if answer == float('inf'):
    print(-1)
else:
    print(answer)