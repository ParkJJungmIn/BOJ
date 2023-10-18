def fast_pow(a, b, mod):
    if b == 0:
        return 1 % mod
    half = fast_pow(a, b // 2, mod)
    
    # b가 짝수일 때
    if b % 2 == 0:
        return (half * half) % mod
    # b가 홀수일 때
    else:
        return (half * half * a) % mod
    
    
N,M,K = map(int,input().split())
print(fast_pow(N, M, K))