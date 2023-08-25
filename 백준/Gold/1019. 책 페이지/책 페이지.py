N = int(input())

num = 1
answer = [0] * 10

def cal(n):
    while n % 10 != 9:
        for i in str(n):
            answer[int(i)] += num
        n -= 1

    return n

while N > 0:

    N = cal(N)

    if N < 10:
        for i in range(N+1):
            answer[i] += num
    else:
        for i in range(10):
            answer[i] += (N//10 + 1) * num
    answer[0] -= num
    num *= 10
    N //= 10

print(*answer)