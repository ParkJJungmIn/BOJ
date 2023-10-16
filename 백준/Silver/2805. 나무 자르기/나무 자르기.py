N, target = map(int, input().split())

tree = list(map(int,input().split()))

start, end = 0, max(tree)

cut = 0

while start <= end :
    total = 0
    mid = ( start + end ) // 2

    total += sum([  t- mid for t in tree if t > mid])

    if total < target :
        end = mid - 1
    else : 
        cut = mid
        start = mid + 1

print(cut)