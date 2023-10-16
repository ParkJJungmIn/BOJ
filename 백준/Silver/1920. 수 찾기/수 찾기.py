N = int(input())
n_num = list( map(int,input().split()) )
M = int(input())
m_num = list(map(int, input().split()))
n_num.sort()

for m in m_num:
    tmp = 0
    left, right = 0, N-1
    while left <= right:
        mid = (left+right) // 2

        if n_num[mid] == m :
            tmp = 1
            break
        elif n_num[mid] < m :
            left = mid+1
        else:
            right = mid-1
    print(tmp)