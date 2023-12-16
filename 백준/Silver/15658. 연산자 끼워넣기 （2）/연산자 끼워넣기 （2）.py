N = int(input())
a = list(map(int,input().split()))
symbol = list(map(int,input().split()))
max_ans = -float('inf')
min_ans = float('inf')

def dfs(idx, ans):
    global max_ans,min_ans
    
    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    
    if symbol[0] > 0:
        symbol[0] -= 1
        dfs(idx+1, ans+a[idx])
        symbol[0] += 1
    if symbol[1] > 0:
        symbol[1] -= 1
        dfs(idx+1, ans-a[idx])
        symbol[1] += 1
    if symbol[2] > 0:
        symbol[2] -= 1
        dfs(idx+1, ans*a[idx])
        symbol[2] += 1
    if symbol[3] > 0:
        symbol[3] -= 1
        dfs(idx+1, int(ans/a[idx]))
        symbol[3] += 1
        
dfs(1,a[0])
print(max_ans)
print(min_ans)
