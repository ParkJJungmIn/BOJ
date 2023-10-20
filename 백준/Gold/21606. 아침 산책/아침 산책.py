from collections import defaultdict, deque

N = int(input())
can_root = list(input())

def bfs(start):
    visited = [False] * (N+1)
    q = deque([(start, [start])])
    count = 0
    
    while q:
        current, path = q.popleft()
        visited[current] = True

        for next_node in graph[current]:
            # 이미 방문한 노드는 무시
            if visited[next_node]:
                continue

            # 다음 노드가 실내라면, 그 노드에서 더 이상 경로를 탐색하지 않고 경로 수만 추가
            if can_root[next_node-1] == '1':
                count += 1
                continue
            
            # 다음 노드가 실외라면, 해당 노드를 큐에 추가하고 탐색을 계속 진행
            q.append((next_node, path + [next_node]))
            
    return count

graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
# 실내인 노드만 시작점으로 설정하고 bfs 수행
for i in range(1, N+1):
    if can_root[i-1] == '1':
        answer += bfs(i)

print(answer)