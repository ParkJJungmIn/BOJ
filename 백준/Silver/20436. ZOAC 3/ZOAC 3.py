keyboard = [
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']
    ]
only_left = 'yuiophjklbnm'

from collections import defaultdict

keyboard_dict = defaultdict(tuple)

for i in range(len(keyboard)):
    for j, key in enumerate(keyboard[i]):
        keyboard_dict[key] = (i,j)


left,right = map(str, input().split())
key_typing = list(input())

answer = 0
for key in key_typing:  
    answer += 1
    if key not in only_left:
        tmp_left = abs(keyboard_dict[left][0]-keyboard_dict[key][0]) + abs(keyboard_dict[left][1]-keyboard_dict[key][1])
        answer += tmp_left
        left = key
    else:
        tmp_right = abs(keyboard_dict[right][0]-keyboard_dict[key][0]) + abs(keyboard_dict[right][1]-keyboard_dict[key][1])
        answer += tmp_right
        right = key
    

print(answer )