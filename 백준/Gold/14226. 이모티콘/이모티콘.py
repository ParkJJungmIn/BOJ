from collections import deque

def find_min_time(target_count):
    time_cost = [[-1] * (target_count + 1) for _ in range(target_count + 1)]
    queue = deque([(1, 0)])
    time_cost[1][0] = 0

    while queue:
        screen, clipboard = queue.popleft()

        if screen == target_count:
            return time_cost[screen][clipboard]

        # 1. 화면에 있는 이모티콘을 클립보드에 복사
        if time_cost[screen][screen] == -1:
            time_cost[screen][screen] = time_cost[screen][clipboard] + 1
            queue.append((screen, screen))

        # 2. 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if screen + clipboard <= target_count and time_cost[screen + clipboard][clipboard] == -1:
            time_cost[screen + clipboard][clipboard] = time_cost[screen][clipboard] + 1
            queue.append((screen + clipboard, clipboard))

        # 3. 화면에 있는 이모티콘 중 하나를 삭제
        if screen - 1 >= 0 and time_cost[screen - 1][clipboard] == -1:
            time_cost[screen - 1][clipboard] = time_cost[screen][clipboard] + 1
            queue.append((screen - 1, clipboard))

    return min(time for time in time_cost[target_count] if time != -1)

target_count = int(input())
print(find_min_time(target_count))
