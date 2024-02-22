from collections import deque

T = int(input())
for _  in range(T):
    command = input()
    N = int(input())
    nums = deque(eval(input()))

    mode = 'L'

    for c in command:
        isError = False
        
        if c == 'R':
            mode = 'R' if mode == 'L' else 'L'

        if c == 'D':
            try:
                if mode == 'R':
                    nums.pop()
                else:
                    nums.popleft()
            except:
                isError = True
                break
    
    if isError:
        print('error')
        continue
    
    if mode == 'R':
        print('[' + ','.join(str(n) for n in list(nums)[::-1]) +']')
    else:
        print( '[' + ','.join(str(n) for n in list(nums)) + ']')