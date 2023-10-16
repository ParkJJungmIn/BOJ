N = int(input())

s = []
for n in range(N):
    i = input()
    s.append( ( len(i), i) )

s = sorted( s , key= lambda x: (x[0],x[1]) )

dup = []

for i in range(N):
    if s[i][1] not in dup:
        dup.append( s[i][1] )
        print(s[i][1])