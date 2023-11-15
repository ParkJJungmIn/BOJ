N = int(input())
fx,fy = map( int ,input().split())

from collections import defaultdict

find_dict = defaultdict(int)
start = (float('inf'),float('inf'))

for n in range(N):
    x,y = map( int ,input().split())
    find_dict[(x,y)] = 1

answer  = 0
for x,y in sorted(find_dict.keys()):
    if find_dict[(x+fx,y)] and find_dict[(x+fx,y+fy)] and find_dict[(x,y+fy)]:
         answer += 1

print(answer)