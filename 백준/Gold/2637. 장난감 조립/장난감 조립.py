N = int(input())
M = int(input())

from collections import defaultdict, deque
graph = defaultdict(list)

for i in range(M):
    x,y,k = map(str,input().split())
    graph[x].append([y,int(k)])

child_count = defaultdict(int)
child_sum = defaultdict(int)

for child_list in graph.values():
    for child in child_list:
        child_count[child[0]] += 1

queue = deque( [ i for i in range(1,N+1) if child_count[str(i)] == 0])

result = defaultdict(int)

row_list = []

while queue:
    node = queue.popleft()
    node_sum = 1 if not child_sum[str(node)] else child_sum[str(node)] 

    if graph[str(node)]:
        for child in graph[str(node)]:
            # print(child)
            child_count[child[0]] -= 1
            child_sum[child[0]] += child[1] * node_sum
            # print( child[0], node , 'node_sum', child[1], node_sum, child_sum)
            if child_count[child[0]] == 0:
                queue.append(child[0])
    else:
        row_list.append(int(node))
            
row_list.sort()

for r in row_list:
    print(r, child_sum[str(r)])