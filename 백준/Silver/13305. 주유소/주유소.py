N = int(input())
distance = list(map(int,input().split()))

price = list(map(int,input().split()))

answer = 0

tmp_price = price[0]

for i in range(N-1):
    answer += tmp_price * distance[i]
    # 가격이 더 높을 경우
    if tmp_price > price[i+1]:
        tmp_price = price[i+1]

print(answer)