a = ['']+list(input())
b = ['']+list(input())

# print(a)

dp = [  [0] * (len(b)) for _ in range(len(a))]

for ia in range( 1, len(a) ):
    for ib in range( 1, len(b)):
        if a[ia] == b[ib]:
            dp[ia][ib] = max(dp[ia-1][ib], dp[ia-1][ib-1] + 1)
        else:
            dp[ia][ib] = max(dp[ia-1][ib], dp[ia][ib-1] )

print(dp[-1][-1])