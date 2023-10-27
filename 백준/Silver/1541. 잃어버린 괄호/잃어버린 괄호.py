cal_str = input()


cal_str = cal_str.split('-')

cal_str = [ sum(list(map(int,c.split('+') )))  for c in cal_str]
# print(cal_str)
for i in range(1, len(cal_str)):
    cal_str[i] *= -1

print(sum(cal_str))