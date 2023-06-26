N,M = map(int, input().split())

info = [True] * (N+1)
info[1] = False

count = 0

for i in range(2, N+1):
    for j in range(i, N+1,i):
        if info[j]:
            info[j] = False
            count += 1
            if count == M:
                print(j)
                exit()