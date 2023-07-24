N,M,K = map(int,input().split())

lines = list(map(int,input().split()))

left = 0
right = lines[K-1] - lines[0]
pivot = 0

while left <= right :
    mid = (right + left) // 2
    tmp = lines[0]
    position = 1
    cnt = 1

    while position < K :

        if lines[position] - tmp < mid:
            position += 1
        else:
            cnt += 1
            tmp = lines[position]
            position += 1

    if cnt < M :
        right = mid-1
    else:
        pivot = max(pivot, mid)
        left = mid+1


answer = ['1']
tmp = lines[0]
cnt = 1

for position in range(1,K):
    if lines[position]-tmp >= pivot and cnt != M:
        answer.append('1')
        tmp = lines[position]
        cnt += 1
    else:
        answer.append('0')

print( ''.join(answer) )