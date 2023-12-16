N,M = map(int,input().split())

test_list = list(map(int,input().split()))

start = 0
end = sum(test_list)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    sum = 0
    for i in range(N):
        sum +=  test_list[i]
        if sum >= mid:
            sum = 0
            cnt += 1
        

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)