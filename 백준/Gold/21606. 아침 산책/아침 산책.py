from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def DFS(v:int):
    indoor = 0
    for i in net[v]:
        if A[i-1] == 0:
            if i not in visited:
                visited.add(i)
                indoor += DFS(i)
        else: indoor += 1

    return indoor


N = int(input())
A = list(map(int, list(input()))) # 장소 n에 대하여 A[n-1]이 1이면 실내, 0이면 실외.
net = defaultdict(list)
route_count = 0

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    net[u].append(v)
    net[v].append(u)
    if A[u-1] == 1 and A[v-1] == 1:
        route_count += 2 # 실내끼리 인접했을 경우 경로를 2개 더해준다.

visited = set()
for i in range(1, N+1):
    indoor = 0
    if A[i-1] == 0:
        if i not in visited:
            visited.add(i)
            indoor = DFS(i)

    route_count += indoor*(indoor-1)

print(route_count)