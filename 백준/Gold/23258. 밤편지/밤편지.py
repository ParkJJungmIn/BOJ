import sys
input = sys.stdin.readline

INF = float('inf')

def init(n, arr):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or i == k or k == j:
                    arr[i][j][k] = arr[i][j][k-1]
                else:
                    arr[i][j][k] = min(arr[i][j][k-1], arr[i][k][k-1] + arr[k][j][k-1])


n, q = map(int, input().split())
arr = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
# [ print(a) for a  in arr]
# print(arr[0][1])
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j][0] = temp[j-1]
        if arr[i][j][0] == 0:
            arr[i][j][0] = INF

init(n, arr)


res = []
for _ in range(q):
    c, s, e = map(int, input().split())
    res.append(str(0 if s==e else (-1 if arr[s][e][c-1] == INF else arr[s][e][c-1])))

print('\n'.join(res))