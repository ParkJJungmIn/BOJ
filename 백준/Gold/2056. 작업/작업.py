N = int(input())


costs = [0] * (N)

inde = [0] * N
dp = [0] * N

graph = [ [] for _ in range(N) ]

for i in range(N):
    a = list(map(int,input().split()))
    costs[i] = a[0]
    for j in a[2:]:
        graph[j-1].append(i)
        inde[i] += 1

from collections import deque
q = deque()

for i, v in enumerate(inde):
    if v == 0:
        q.append(i)
        dp[i] = costs[i]

while q:
    now = q.popleft()

    for next in graph[now]:
        
        inde[next] -= 1
        dp[next] = max(dp[now] + costs[next], dp[next])
        if inde[next] == 0:
            q.append(next)

print(max(dp))