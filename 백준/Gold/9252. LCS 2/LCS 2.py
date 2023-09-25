a = [0] + list(input())
b = [0] + list(input())


dp = [ [0] * (len(b))  for _ in range( len(a)  )]


for a_i in range(1,len(a)):
    for b_i in range(1,len(b)):
        # dp[a_i][b_i] = dp[a_i][b_i-1]

        if a[a_i] == b[b_i]:
            dp[a_i][b_i] = dp[a_i-1][b_i-1]+1
        else:
            dp[a_i][b_i] = max( dp[a_i][b_i-1], dp[a_i-1][b_i])

last_point = dp[-1][-1]
print(last_point)
a_len = len(a)-1
b_len = len(b)-1
max_len = 1
answer = []

while last_point != 0 :
    if dp[a_len][b_len] == dp[a_len][b_len-1]:
        b_len -= 1
    elif dp[a_len][b_len] == dp[a_len-1][b_len]:
        a_len -= 1
    else:
        answer.append( a[a_len] )
        b_len -= 1
        a_len -= 1
        last_point -= 1

answer.reverse()

print(''.join(answer) )