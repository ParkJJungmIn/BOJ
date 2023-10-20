from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

operators = ['+', '-', '*', '/'] * N
operators_count = list(map(int, input().split()))
operators_list = []
for idx, count in enumerate(operators_count):
    operators_list.extend([operators[idx]] * count)

permuted_operators = list(permutations(operators_list, N - 1))
permuted_operators = list(set(permuted_operators))  # 중복 제거

max_val = -float('inf')
min_val = float('inf')

for ops in permuted_operators:
    result = nums[0]
    for i in range(N-1):
        if ops[i] == '+':
            result += nums[i+1]
        elif ops[i] == '-':
            result -= nums[i+1]
        elif ops[i] == '*':
            result *= nums[i+1]
        else:
            if result < 0:
                result = -(-result // nums[i+1])
            else:
                result //= nums[i+1]
    max_val = max(max_val, result)
    min_val = min(min_val, result)

print(max_val)
print(min_val)