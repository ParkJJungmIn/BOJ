import math

def solution(m, n, startX, startY, balls):
    result = []
    for ball in balls:
        if startX == ball[0]:
            width = min(startX, m - startX)
            height = abs(startY - ball[1]) / 2
            direct = (n * 2 - (startY + ball[1])) ** 2 if startY > ball[1] else (startY + ball[1]) ** 2
            result.append(min(
                round((math.sqrt(width**2 + height**2) + math.sqrt(width**2 + height**2)) ** 2),
                direct,
            ))
        elif startY == ball[1]:
            height = min(startY, n - startY)
            width = abs(startX - ball[0]) / 2
            direct = (m * 2 - (startX + ball[0])) ** 2 if startX > ball[0] else (startX + ball[0]) ** 2
            result.append(min(
                round((math.sqrt(width**2 + height**2) + math.sqrt(width**2 + height**2)) ** 2),
                direct,
            ))
        else:
            result.append(min(
                get_distance(abs(startY - ball[1]), startX, ball[0]),
                get_distance(abs(startY - ball[1]), m - startX, m - ball[0]),
                get_distance(abs(startX - ball[0]), startY, ball[1]),
                get_distance(abs(startX - ball[0]), n - startY, n - ball[1]),
            ))
    return result

def get_distance(share_height, width1, width2):
    max_w = max(width1, width2)
    min_w = min(width1, width2)

    max_h = share_height / (max_w + min_w) * max_w
    min_h = share_height / (max_w + min_w) * min_w

    return round((math.sqrt(max_w**2 + max_h**2) + math.sqrt(min_w**2 + min_h**2)) ** 2)