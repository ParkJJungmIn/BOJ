def solution(n, v):
    ans = 0
    for i in range(1, n + 1):
        if v[i + 1] > v[i + 2]:
            a = min(v[i], v[i + 1] - v[i + 2])
            ans += 5 * a
            v[i] -= a
            v[i + 1] -= a

            b = min(v[i], min(v[i + 1], v[i + 2]))
            ans += 7 * b
            v[i] -= b
            v[i + 1] -= b
            v[i + 2] -= b
        else:
            b = min(v[i], min(v[i + 1], v[i + 2]))
            ans += 7 * b
            v[i] -= b
            v[i + 1] -= b
            v[i + 2] -= b

            a = min(v[i], v[i + 1])
            ans += 5 * a
            v[i] -= a
            v[i + 1] -= a
        ans += 3 * v[i]
    return ans

n = int(input())
v = [0] + list(map(int, input().split())) + [0, 0]  # 0-padding for edge cases
print(solution(n, v))