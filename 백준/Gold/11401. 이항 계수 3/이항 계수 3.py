N,K = map(int,input().split())

mod = 1000000007

def factory(n):
    return_input = 1

    for i in range(1,n+1):
        return_input *= i
        return_input %= mod

    return return_input

n = factory(N)
k = factory(K)
nk = factory(N-K)

def sqrt( a , b ):
    if b == 0 :
        return 1
    elif b == 1:
        return a

    tmp = sqrt(a , b // 2)

    if b % 2:
        return tmp * tmp * a % mod
    else:
        return tmp * tmp % mod

print(n * sqrt(k*nk%mod, mod-2) % mod)