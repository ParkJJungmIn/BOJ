N, A, B, C, D = map(int,input().split())

if C*B < A*D :
    A,B,C,D = C,D,A,B

import math

answer = float('inf')

for AB in range(C):
    CD = math.ceil(  (N- A*AB )/ C   )

    if CD < 0 :
        CD = 0
        
    answer = min( answer, (B * AB)+ (D * CD)  )

    if CD == 0 : break

print(answer)