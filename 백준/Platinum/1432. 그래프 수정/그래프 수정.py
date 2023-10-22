from collections import defaultdict
from heapq import heappush, heappop

N = int(input())
graph = defaultdict(list)
degree = [0] * (N+1)
answer = [0] * (N+1)

# 간선 정보 입력 및 차수 증가
for i in range(1, N+1):
    for j, v in enumerate(input()):
        if v == '1':
            graph[j+1].append(i)
            degree[i] += 1

# 차수가 0인 노드를 우선순위 큐에 삽입
q = []
for i in range(1, N+1):
    if degree[i] == 0:
        heappush(q, -i)

N_value = N
while q:
    now = -heappop(q)
    answer[now] = N_value
    N_value -= 1

    for next_node in graph[now]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            heappush(q, -next_node)

# 차수가 0이 아닌 노드가 남아 있으면 -1 출력
if 0 in answer[1:]:
    print(-1)
else:
    print(*answer[1:])