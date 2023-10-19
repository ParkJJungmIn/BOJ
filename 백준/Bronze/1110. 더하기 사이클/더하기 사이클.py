N = input()
tmp = '0' + str(N) if int(N) < 10 else str(N)
cnt = 0

while True:
    tmp2 = int(tmp[0]) + int(tmp[1])
    tmp2 = '0' + str(tmp2) if int(tmp2) < 10 else str(tmp2)
    tmp2 = tmp[1] + tmp2[1]

    cnt += 1
    if int(tmp2) == int(N):
        # print(tmp2)
        print(cnt)
        exit()

    tmp3 = int(tmp[1]) + int(tmp2[1])
    tmp3 = '0' + str(tmp3) if int(tmp3) < 10 else str(tmp3)
    tmp3 = tmp2[1] + tmp3[1]
    # print(cnt, tmp,tmp2,tmp3)
    tmp = tmp3
    
    cnt += 1
    # if cnt == 10:
    #     break
    if int(tmp3) == int(N):
        print(cnt)
        exit()