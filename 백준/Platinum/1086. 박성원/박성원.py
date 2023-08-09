import sys
from math import gcd,factorial
N = int(input())

num_list = [ input() for _ in range(N)]
len_list = [ len(i) for i in num_list]
total_len = sum(len_list)

K = int(input())
dp = [ [-1] * K for _ in range(1<<N)]

mod_list = [ [0] * total_len  for _ in range(N)]

for i in range(N):
    for j in range(total_len):
        mod_list[i][j] = ( int(num_list[i]) * 10 ** j) % K

def dfs( now_len , visited, mod ):
    if visited == (1 << N)-1:
        return 1 if mod == 0 else 0
    
    if dp[visited][mod] != -1:
        return dp[visited][mod]

    for i in range(N):
        if not visited & (1 << i ):
            dp[visited][mod] += dfs( now_len+len_list[i], visited | (1 << i) , (mod_list[i][now_len]+mod) % K  )
    dp[visited][mod] += 1

    return dp[visited][mod]

num = dfs(0,0,0)
denomin = factorial(N)
max_mod = gcd(num,denomin)
print( "0/1" if num == 0 else f"{num // max_mod}/{denomin // max_mod}")