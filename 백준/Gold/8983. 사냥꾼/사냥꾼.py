# |사냥꾼의 x 위치 - 동물의 x 위치| + 동물의 y 
N,M,L = map(int , input().split())

saro = list( map(int, input().split()))
saro.sort()

answer = 0
for n in range(M):
    x,y = map(int, input().split())
    
    # abs(유효거리- y좌표) - x좌표

    left=  x - ( L - y)
    right = x + (L - y) 

    start = 0
    end = len(saro)-1

    while start <= end:
        mid = (start+end )// 2
     
        if left <= saro[mid] <= right:
            answer += 1
            break
    
        if left > saro[mid]:
            start = mid+1
        elif right < saro[mid]:
            end = mid-1

print(answer)