import sys
inpt = sys.stdin.readline

N = int(input())

egg = [ list(map(int,input().split())) for _ in range(N)]

answer = 0

def dfs(now,egg):
    global answer
    # print(egg)
    if now == N:
        answer = max( answer, len([ i for i in range(N) if egg[i][0] <= 0 ]) )
        return

    if egg[now][0] <= 0 :
        dfs(now+1 ,egg)
    else:
        all_check = False
        for next in range(N):
            if egg[next][0] > 0 and now != next:
                egg[now][0] -= egg[next][1]
                egg[next][0] -= egg[now][1]
                dfs(now+1, egg)
                egg[now][0] += egg[next][1]
                egg[next][0] += egg[now][1]
                all_check=True
        if not all_check:
            dfs(N, egg)

dfs(0, egg)
print(answer)