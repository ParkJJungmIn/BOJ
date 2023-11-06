N, M = map(int, input().split())

check_dict = { input():1  for _ in range(N)}

answer = 0

for _ in range(M):
    if check_dict.get(input()):
        answer+=1

print(answer)