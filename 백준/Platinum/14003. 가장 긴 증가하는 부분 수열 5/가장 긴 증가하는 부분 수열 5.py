from collections import deque

def bin_search(a , save ):

    left = -1
    right = len(save)

    while left+1 < right:
        mid = (left + right) // 2

        if a > save[mid]:
            left = mid
        else:
            right = mid
    
    return right

N = int(input())
row = list(map(int,input().split()))

queue = deque(row)

save = [ -float('inf') ]
order = [ (save[0],-1) ]

while queue:
    a = queue.popleft()

    if a > save[-1]:
        order.append( (a,len(save)) )
        save.append(a)
    else:
        idx = bin_search(a,save)
        save[idx] = a
        order.append( (a,idx) )

answer = []
cnt = len(save)-1
for i in range(len(order)-1,-1,-1 ):
    if order[i][1] == cnt:
        answer.append(order[i][0])
        cnt -= 1
answer.reverse()
print(len(save)-1)
print(*answer)