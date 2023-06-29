import sys
input = sys.stdin.readline

T,W = map(int,input().split())

timeline = [ [ 0 for _ in range(W+1)] for _ in range(T+1) ]
treemap = [0] + [ int(input()) for _ in range(T)]
for t in range(1,T+1):
    timeline[t][0]=  timeline[t-1][0]+1 if treemap[t] == 1 else timeline[t-1][0]
    for w in range(1,W+1):
        if w > t: break
        if treemap[t] == 1 and w % 2 == 0:
            timeline[t][w] = max( timeline[t-1][w], timeline[t-1][w-1] ) + 1
        elif treemap[t] == 2 and w % 2 == 1:
            timeline[t][w] = max( timeline[t-1][w], timeline[t-1][w-1] ) + 1
        else:
            timeline[t][w] = max( timeline[t-1][w], timeline[t-1][w-1] ) 
print(max(timeline[-1]))