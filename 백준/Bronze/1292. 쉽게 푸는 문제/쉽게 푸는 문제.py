start,end = map(int,input().split())

n = 0
answer = 0



for i  in range(1,10000):

    if n+i >= end:
        tmp = end - start + 1 if n < start else end - n
        answer += tmp * i
        break

    if n < start <= n+i:
        answer += ((n+i+1) - start ) * i
    elif start < n+i < end:
        answer += i*i
    n = n+i

print(answer)