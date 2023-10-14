N = int(input())
num = [ int(input())  for _ in range(N)]

susoo = sorted(set(range(2, max(num)+1)) - {j for i in range(2, int(max(num)**0.5) + 1) for j in range(i*2, max(num)+1, i)})

def find_answer( tmp ,tarket ):
    tmp_len = len(tmp)
    # print(tmp_len)

    tmp_arr = []
    answer = float('inf')

    for i in range( tmp_len ):

        if  tarket-tmp[i] not in tmp:
            continue
        else:
            tmp_index = tmp.index(tarket-tmp[i])
            # tmp_arr = [ (tmp[i]-tmp_index,tmp) ]

            if answer > abs(tmp[i]-tmp[tmp_index]):
                answer = abs(tmp[i]-tmp[tmp_index])
                tmp_arr = [tmp[i], tmp[tmp_index] ]

    return sorted(tmp_arr)


        # for j in range( tmp_len ):
        #     if tmp[i] + tmp[j] == tarket:
        #          tmp_arr.append(sorted([tmp[j], tmp[i]]))

    

    # for i in range(tmp_len//2 , tmp_len ):
    #     for j in range( tmp_len-1 ,-1,-1):
    #         if tmp[i] + tmp[j] == tarket:
    #             return sorted([tmp[j], tmp[i]])

for n in num:
    cnt = float('inf')
    tarket = n
    answer = 0
    tmp = []
    for s in susoo:
        if s <= tarket:
            tmp.append(s)
        else:
            break

    answer = find_answer(tmp, tarket)
    print(answer[0], answer[1])