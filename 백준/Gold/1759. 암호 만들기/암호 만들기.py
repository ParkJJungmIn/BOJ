N,M = map(int, input().split())
texts = input().split(' ')

mo = ['a', 'e', 'i', 'o' , 'u']

from itertools import combinations
now_mo = [ t for t in texts if t in mo]
now_texts = list(set(texts)-set(now_mo))

answer = []
for i in range(len(now_mo)):
    i += 1
    com = list(combinations(now_mo, i))
    
    if N-i < 0: continue

    com2 = list(combinations(now_texts, N-i))

    for c1 in com:
        for c2 in com2:
            if len(c2) < 2:continue
            
            t= sorted(list(c2) + list(c1)) 
            answer.append(''.join(t))


answer.sort()
[ print(a) for a in answer]