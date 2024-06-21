N = input()

change_list = list(input())

last_char = change_list[-1]

while change_list:
    if last_char == change_list[-1]:
        change_list.pop()
    else:
        break

answer = [change_list.count('R'), change_list.count('B')]

print(min(answer))