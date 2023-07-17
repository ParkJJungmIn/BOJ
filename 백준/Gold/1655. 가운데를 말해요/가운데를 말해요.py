from heapq import heappush, heappop

import sys

input = sys.stdin.readline

N = int(input())

left = []
right = []

for _ in range(N):

    add = int(input())

    if len(left) == len(right):
        heappush(left, -add)
        # left.append( add )
    else:
        heappush(right, add)
        # right.append( -add )

    if left and right and -left[0] > right[0]:
        l = -heappop(left)
        r = heappop(right)

        heappush(left, -r)
        heappush(right,l)
    print(-left[0])
