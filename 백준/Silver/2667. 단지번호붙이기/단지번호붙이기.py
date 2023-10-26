N = int(input())

apt = []
for _ in range(N):
    apt.append(input())

visited = [ [0] * N for _ in range(N)]

floor = 1
apt_counts = []

def dfs(xy):
    stack = [xy]
    apt_count = 0
    while stack:
        x, y = stack.pop()
        if visited[y][x] == 0 and apt[y][x] == '1':
            visited[y][x] = floor
            apt_count += 1
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    stack.append((nx, ny))
    return apt_count

for y, apt_y in enumerate(apt):
    for x, apt_x in enumerate(apt_y):
        if apt_x == '1' and visited[y][x] == 0:
            apt_counts.append(dfs((x, y)))
            floor += 1

apt_counts.sort()

print(len(apt_counts))
for count in apt_counts:
    print(count)