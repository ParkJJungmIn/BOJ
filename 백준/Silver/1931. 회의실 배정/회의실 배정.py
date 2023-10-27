N = int(input())

meet_list = [ tuple(map(int,input().split())) for _ in range(N)]

meet_list.sort()

now_meet = meet_list[0]
answer = 1
for j in range(1,len(meet_list)):
    
    if now_meet[1] <= meet_list[j][0]:
        answer += 1
        now_meet = meet_list[j]
    elif now_meet[1] > meet_list[j][1]:
        now_meet = (now_meet[0],meet_list[j][1])

print(answer)