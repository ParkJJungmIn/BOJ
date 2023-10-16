from itertools import combinations
s = []
for i in range(9):
    s.append( int(input()) )

for i in list(combinations(s,7)):
    if sum(i) == 100:
        [ print(j) for j in sorted(i)]
        break