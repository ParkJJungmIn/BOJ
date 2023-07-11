from collections import deque
while True:
    rows = list(map(int, input().split()))
    if rows[0] == 0:
        break

    N = rows[0]
    stack = deque()

    answer = -1

    for index,i in enumerate(rows):
        if index == 0 : continue

        while stack and stack[-1][1] > i :

            tmp_index, tmp_height = stack.pop()

            start = 1
            if stack:
                start = stack[-1][0] + 1
            answer = max( (index - start) * tmp_height , answer )
  
        if not stack or stack[-1][1] <= i:
            stack.append( (index, i) )


    while stack:
        tmp_index, tmp_i = stack.pop()
        
        start = 1
        if stack:
            start = stack[-1][0] + 1
        answer = max( ( (N+1 - start) * tmp_i  ) , answer )

    print(answer)