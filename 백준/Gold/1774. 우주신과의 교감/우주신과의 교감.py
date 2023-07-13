import sys
input = sys.stdin.readline

N,M = map(int,input().split())

parent = list(range(N+1))

g_d = {}
for n in range(N):
    a,b = map(int,input().split())
    g_d[n+1] = (a,b)

def find(a,parent):

    if parent[a] != a:
        parent[a] = find(parent[a], parent)
    
    return parent[a]

for m in range(M):
    a,b = map(int,input().split())
    
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        a,b = b,a

    if a != b:
        parent[a] = b

cost = []

for a in range(1,N):
    for b in range(a+1, N+1):
        cost.append( (( (   g_d[a][0] - g_d[b][0] ) ** 2 + (  g_d[a][1] - g_d[b][1] ) ** 2) ** 0.5  , a,b ) )

cost.sort()

answer = 0
for c,a,b in cost:
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        a,b = b,a

    if a != b:
        parent[a] = b
        answer += c

print(f"{answer:.2f}") 