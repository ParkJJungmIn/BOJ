R,C,W = map(int , input().split()) 

pascal_list = [ [1] * i for i in range(1,32)]
for i in range(2,31):
    for j in range(1,i):

        if pascal_list[i-1][j-1] == 1:
            pascal_list[i][j] += pascal_list[i-1][j] 
        elif pascal_list[i-1][j] == 1:
            pascal_list[i][j] += pascal_list[i-1][j-1] 
        else:
            pascal_list[i][j] = pascal_list[i-1][j] + pascal_list[i-1][j-1]


answer = 0

j = C
for i in range(R-1, R+W-1):
    for z in range(C-1,j):
        answer += pascal_list[i][z] 
    j += 1

print(answer)