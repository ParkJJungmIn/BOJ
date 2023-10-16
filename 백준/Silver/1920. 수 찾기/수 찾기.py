N = int(input())

data_dict = {}
for i in input().split():
    data_dict[i] = 1

M = int(input())
find_list = input().split()

for f in find_list:
    if data_dict.get(f):
        print(1)
    else:
        print(0)