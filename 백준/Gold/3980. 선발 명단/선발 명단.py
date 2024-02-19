N = int(input())
for _ in range(N):
    players = [ list(map(int,input().split(' ')))for _ in range(11)]
    temp = 0
    def dfs(count, position):
        global temp

        if count == 11:
            temp = max(sum(position),temp)
            return
        
        for i in range(11):
            if players[count][i] != 0 and position[i] == 0:
                
                position[i] = players[count][i]
                dfs(count+1, position)
                position[i] = 0

    dfs(0, [ 0 for _ in range(11)] )
    print(temp)