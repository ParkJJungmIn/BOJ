N = int(input().strip())
A = list(map(int, input().strip()))
graph = [[] for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

count = 0

def dfs(curr, prev):
    global count

    if A[curr] == 1 and curr != prev:
        count += 1
        return
    
    for neighbor in graph[curr]:
        if neighbor != prev:
            dfs(neighbor, curr)

for i in range(N):
    if A[i] == 1:
        dfs(i, i)

print(count)
