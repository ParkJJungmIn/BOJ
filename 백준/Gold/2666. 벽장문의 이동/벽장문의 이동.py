N = int(input())
a,b = map(int,input().split())
M = int(input())

door_ma = [1]+[ 0 if i in [a,b] else 1 for i in range(1,N+1)]

visited = [-1] + [ int(input()) for i in range(M)]
answer = float('inf')

def dfs(now, cnt, door_map):
    global answer
    if now == M+1:
        answer = min(answer, cnt)
        return
    
    now_v = visited[now]
    for i in range(N+1):
        if door_map[i]==0:
            tmp_map = door_map[:]
            tmp_map[now_v],tmp_map[i] = tmp_map[i],tmp_map[now_v]
            dfs(now+1, cnt+abs(now_v-i) , tmp_map)

dfs(1,0,door_ma)
print(answer)