from heapq import heappop, heappush

N,G,K = map(int, input().split())

material = [  list(map(int,input().split()))  for _ in range(N)]

left = 1
right = int(2e9)

answer = 0

while left <= right:
    mid = (left + right) // 2
    max_g = []
    h_m = []
    for m in material:
        si_max = m[0] * max(1, mid - m[1]  )
        if m[2] == 1:
            heappush(h_m, -si_max )
        else:
            max_g.append( si_max )
    
    for _ in range(K):
        if h_m:
            heappop(h_m)

    total = sum( max_g) + sum([ m1 * -1 for m1 in h_m])
    
    # print(left, right, total)
    if G < total:
        right = mid -1
    else:
        answer = max(answer, mid)
        left = mid + 1

print(answer)