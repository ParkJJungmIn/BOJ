import sys
sys.setrecursionlimit(10**5)


N = int(input())

state_list = list(map(int ,list(input()) ))

from collections import defaultdict
graph = defaultdict(list)

answer = 0

for _ in range(N-1):
    a,b = map(int , input().split() )

    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

    if state_list[a-1] == 1 and state_list[b-1] == 1:
        answer += 2

visited = [0] * N


def dfs(start):
    count = 0
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0 and state_list[i] == 0:
            count += dfs(i)
        elif state_list[i] == 1:
            count += 1
    
    return count


for i in range(N):
    if state_list[i] == 0 and visited[i] == 0:
        tmp_cnt = dfs(i)
        answer += (tmp_cnt) * (tmp_cnt-1)

print(answer)