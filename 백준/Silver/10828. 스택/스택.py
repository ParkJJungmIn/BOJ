import sys

N = int(input())

func = {
    'push' : lambda a,b : a.append(b),
    'top' : lambda b : print(-1) if len(b) == 0 else print(b[-1]),
    'size' : lambda a : print(len(a)),
    'pop' : lambda a : print(-1) if len(a) == 0 else print(a.pop()) ,
    'empty' : lambda a : print( 1 if not len(a) else 0 )
}

stack = []

for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if len(command) == 1:
        func[command[0]](stack)
    else:
        func[command[0]](stack,command[1])

exit()