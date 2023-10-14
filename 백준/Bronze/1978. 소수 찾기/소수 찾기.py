N = input()

num_list = list( map(int, input().split() ))
cnt = 0
for n in num_list:
    if 2 == sum([  1 if n%i == 0  else 0 for i in range(1,n+1)]) :
        cnt += 1
print(cnt)