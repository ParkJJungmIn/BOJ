N,B = map(int,input().split())

board = [ list(map(int,input().split())) for n in range(N)]

def mul( a, b):
    tmp_b = [ [0] * len(a) for _ in range( len(a) ) ]

    for row in range( len(a) ):
        for col in range( len(a) ):
            tmp = 0
            for multi in range(len(a)):
                tmp += a[row][multi] * b[multi][col]
            tmp_b[row][col] = tmp % 1000
    
    return tmp_b

def sqrt(a,b):
    
    if b == 1:
        for row in range(len(a)):
            for col in range(len(a)):
                a[row][col] %= 1000
        
        return a
    
    tmp = sqrt(a, b//2)

    if b % 2:
        return mul( mul(tmp,tmp), a )
    else:
        return mul(tmp,tmp)

answer = sqrt(board,B)

[ print(*a) for a in answer]