N,L = map(int, input().split())

nums = list(map(int, input().split()))

from heapq import heappush, heappop


h = []

for i in range(N):

    heappush(h,(nums[i], i))

    while h and i-L >= h[0][1]:
        heappop(h)
    
    print(h[0][0])