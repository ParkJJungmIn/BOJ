N = int(input())

line_q = [  int(input()) for _ in range(N)]

count = 0
answer = 1
line_set = list(set(line_q))

while line_set:
    continue_text = line_set.pop()
    tmp_text = None
    tmp_count = 1
    for line_text in line_q:
        if continue_text == line_text:
            continue

        if tmp_text == line_text:
            tmp_count += 1
            if tmp_count > answer:
                answer = tmp_count
        else:
            tmp_count = 1

        tmp_text = line_text
print(answer)