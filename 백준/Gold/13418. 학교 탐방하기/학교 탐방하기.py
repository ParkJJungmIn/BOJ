N,M = map(int,input().split())

graph = []


for _ in range(M+1):
    a,b,c = map(int, input().split())
    graph.append( [c,(a,b)])

graph.sort()

def find_parent(a,parent):

    if parent[a] != a:
        parent[a]= find_parent(parent[a], parent)

    return parent[a]

def find(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)
    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        return True
    else:
        return False

parent = [ i for i in range(N+1)]

up_score = 0

for upDown,(a,b) in graph:
    checked = find(a,b,parent)
    if checked and upDown == 0 :
        up_score += 1


down_score = 0

graph.sort(reverse=True)
parent = [ i for i in range(N+1)]

for upDown,(a,b) in graph:
    checked = find(a,b,parent)
    if checked and upDown == 0 :
        down_score += 1


print( abs((down_score ** 2 ) - (up_score ** 2)) )