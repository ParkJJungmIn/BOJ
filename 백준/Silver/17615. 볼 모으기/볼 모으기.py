def color_count(change_list):
    cnt = 0
    for i in range(N-1):
        if change_list[i] != change_list[0]:
            break
        cnt += 1
    return cnt

N = int(input())
change_list = list(input())

red = change_list.count('R')
blue = change_list.count('B')

answer = min(red,blue)

cnt = color_count(change_list)
r_cnt = color_count( change_list[::-1] )

if change_list[0] == 'R':
    answer = min(answer, red-cnt)
if change_list[-1] == 'R':
    answer = min(answer, red-r_cnt)
if change_list[0] == 'B':
    answer = min(answer, blue-cnt)
if change_list[-1] == 'B':
    answer = min(answer, blue-r_cnt)


print(answer)