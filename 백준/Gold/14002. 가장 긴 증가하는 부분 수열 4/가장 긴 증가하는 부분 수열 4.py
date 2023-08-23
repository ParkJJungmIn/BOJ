N = int(input())
row = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if row[i] > row[j] :
            dp[i] = max(dp[i], dp[j]+1)

answer = max(dp)
answer_list = []
print(answer)
for i in range(N-1,-1,-1):
    if dp[i] == answer :
        answer_list.append(row[i])
        answer -= 1
answer_list.reverse()
print(*answer_list)