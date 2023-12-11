ab_list = input().split('.')

for idx, ab in enumerate(ab_list):
    
    ab_len = len(ab)
    re = ""

    if ab == '':
        continue
    if len(ab) % 2 != 0:
        print('-1')
        exit()
    else:
        if ab_len // 4 >= 1:
            re += "AAAA" * ( ab_len // 4 )
            ab_len -= len(re)
            if ab_len != 0:
                re += "BB"
        else:
            re += "BB"

    ab_list[idx] = re

print('.'.join(ab_list))
