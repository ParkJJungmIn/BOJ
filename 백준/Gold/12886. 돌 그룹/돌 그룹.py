abc = list(map(int, input().split()))
abc.sort()

abc = tuple(abc)
from collections import deque
visited = set()
visited.add(abc)

def bfs(abc):
    queue = deque([abc])

    while queue:
        abc = queue.popleft()
        if abc[0] == abc[1] == abc[2]:
            print(1)
            exit()
        
        for i in range(2):
            for j in range(i+1,3):
                tmp_abc = list(abc)
                tmp_abc[i], tmp_abc[j] = tmp_abc[i] * 2, tmp_abc[j] - tmp_abc[i]
                tmp_abc.sort()
                tmp_abc = tuple(tmp_abc)
                if tmp_abc not in visited:
                    visited.add(tmp_abc)
                    queue.append(tmp_abc)
bfs(abc)
print(0)