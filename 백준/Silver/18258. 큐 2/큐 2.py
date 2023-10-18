N = int(input())

func = {
    'push' : lambda a, b: a.appendleft(int(b)),  # b를 int로 변환하여 추가
    'pop' : lambda a:  print(-1) if not len(a) else print(a.pop()),
    'size' : lambda a: print(len(a)),
    'empty' : lambda a: print(1 if len(a) == 0 else 0),
    'front' : lambda a: print(a[-1]) if len(a) != 0 else print(-1),
    'back' : lambda a: print(a[0]) if len(a) != 0 else print(-1)
}

from collections import deque
import sys
q = deque()
for n in range(N):
    i = sys.stdin.readline().rstrip().split()
    if len(i) == 1:
        func[i[0]](q)
    else:
        func[i[0]](q, i[1])