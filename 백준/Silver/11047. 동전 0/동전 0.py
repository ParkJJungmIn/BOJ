N, K = map(int,input().split())

coin = [ int(input()) for _ in range(N)]

answer = 0

while K > 0:
    last_index = 0
    for i,c in enumerate(coin):
        # print(i,c)
        if K >= coin[i]:
            last_index = i
        
    answer += (K // coin[last_index])
    K -= (K // coin[last_index]) * coin[last_index]

print(answer)