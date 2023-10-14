
n = int(input())

# from itertools import combinations
answer = n
for i in range(n-1, 0, -1):
    answer *= i
print( 1 if n == 0 else answer) 