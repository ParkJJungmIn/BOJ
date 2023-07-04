import sys
input = sys.stdin.readline

month = { **dict.fromkeys([4,6,9,11] , 30 ),
**dict.fromkeys([1, 3, 5, 7, 8, 10, 12] , 31 ),
**dict.fromkeys([2] , 28 ),
}

month_cal = {}

total = 0
for i in range(1,13):
    month_cal[i] = total
    total += month[i]

start = month_cal[3] + 1
end = month_cal[12]
N = int(input())

timeline = []

for _ in range(N):
    a,b,c,d = map(int,input().split())

    timeline.append( [ month_cal[a] + b , month_cal[c] + d ] )
timeline.sort( key = lambda a : a[0] )

m = 0
count = 0
for i in range( len(timeline) ):
    if timeline[i][0] <= start :
        if timeline[i][1] > m:
            m = timeline[i][1]

if m != 0:
    count += 1

tmpm = m

while m <= end:

    for i in range( len(timeline) ):
        if timeline[i][0] <= m:
            if tmpm < timeline[i][1]:
                tmpm = timeline[i][1]
        else:
            break
    
    if m == tmpm :
        count = 0
        break

    m = tmpm
    count += 1

print(count)