N = list(input())

# nums = [ (N[i], i) for i in range(len(N))]

answer = ['' for _ in range(len(N))]
def sol(arr, idx):
    if not arr:
        return
    min_val = min(arr)
    min_idx = arr.index(min_val)
    answer[min_idx + idx] = min_val
    print(''.join(answer))

    sol(arr[min_idx+1:],idx+min_idx+1)
    sol(arr[:min_idx], idx)

sol(N,0)