N = int(input())

from heapq import heappop,heappush,heapify
from collections import defaultdict

import sys
input = sys.stdin.readline

check = defaultdict()

for _ in range(N):
    maxh = []
    minh = []
    M = int(input())

    for i in range(M):
        command, num = map(str,input().split())
        
        if command == 'I':
            num = int(num)
            heappush(maxh, (-num, i) )
            heappush(minh,(num,i))
            check[i] = True
        elif command == 'D':
            if num == '1':
                while maxh and not check[maxh[0][1]]:
                    heappop(maxh)
                if maxh :
                    check[maxh[0][1]] = False
            else:
                while minh and not check[minh[0][1]]:
                    heappop(minh)
                if minh:
                    check[minh[0][1]] = False

    while maxh and not check[maxh[0][1]]:
        heappop(maxh)
    
    while minh and not check[minh[0][1]]:
        heappop(minh)

    if maxh and minh:
        print(-maxh[0][0] , minh[0][0])
    else:
        print('EMPTY')