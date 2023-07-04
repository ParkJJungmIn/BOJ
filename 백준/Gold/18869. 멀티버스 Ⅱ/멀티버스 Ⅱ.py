import sys
input = sys.stdin.readline
N,M = map(int,input().split())
from collections import defaultdict
order_count = defaultdict(int)
for _ in range(N):
    input_list = list(map(int, input().split()))
    sorted_indices = tuple(index for index, value in sorted(enumerate( list(set(input_list))), key=lambda x: x[1]))
    order_count[sorted_indices] += 1
duplicates = sum( count * (count-1) // 2 for count in order_count.values() if count > 1)

print(duplicates)