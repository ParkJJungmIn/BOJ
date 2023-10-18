from heapq import heappop, heappush
import sys

N = int(input())

n_list = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(n_list) == 0:
            print(0)
        else:
            print(heappop(n_list) * -1)
    else:
        heappush(n_list, -num)