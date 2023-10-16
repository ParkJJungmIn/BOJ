N = int(input())

board = [ list(map( int, input().split())) for _ in range(N) ]

from itertools import permutations

com = list(permutations( range(1,N) , N-1  ))

ans = float('inf')


def check( com_row ):
    start = 0
    answer = 0

    for com in com_row:
        if board[start][com] == 0:
            return -1
        answer += board[start][com]
        start = com

    if board[start][0] == 0:
        return -1
    answer += board[start][0]
    return answer


for c in com:
    r = check(c)
    if r == -1:
        continue
    ans = min(r,ans)

print(ans)