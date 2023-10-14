N = int(input())

for _ in range(N):
    a,b = input().split()
    print(''.join([  b[i] * int(a) for i in range( len(b) )]))