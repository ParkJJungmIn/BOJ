def solution(numbers, target):
    answer = 0
    
    answer = dfs(0,0,numbers,target)
    
    return answer

def dfs(num,cnt,numbers,target):
    
    if cnt == len(numbers):
        if num == target:
            return 1
        else:
            return 0
    
    answer = 0
    
    for i in range(1,3):
        if i % 2 :
            answer += dfs(num+numbers[cnt], cnt+1, numbers, target)
        else:
            answer += dfs(num+ (numbers[cnt] * -1), cnt+1, numbers, target)
    
    return answer

'''
n개의 음(-) 이 아닌 정수.
정수 순서 안바꾸고 적절히 더하거나 빼서 타켓넘버(?) ex) [1,1,1,1,1] 로 숫자 3 만들기

[4,1,2,1] => 4 만들기 -> 몇가지 방법 있는지

[ [True], [True] ]
[ ]

'''