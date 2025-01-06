def heart(find):
    for i in range(N):
        for j in range(N):
            if find[i][j] == "*":
                return i + 2, j + 1

def left_hand(find, heart):
    y, x = heart
    cnt = 0
    for j in range(x-1):
        if find[y-1][j] == "*":
            cnt += 1
    return cnt

def right_hand(find, heart):
    y, x = heart
    cnt = 0
    for j in range(x, N):
        if find[y-1][j] == "*":
            cnt += 1
    return cnt

def waist(find, heart):
    y, x = heart
    cnt = 0
    for i in range(y, N):
        if find[i][x-1] == "*":
            cnt += 1
    return cnt

def left_leg(find, heart, waist_length):
    y, x = heart
    cnt = 0
    start_y = y + waist_length
    for i in range(start_y, N):
        if find[i][x-2] == "*":
            cnt += 1
    return cnt

def right_leg(find, heart, waist_length):
    y, x = heart
    cnt = 0
    start_y = y + waist_length
    for i in range(start_y, N):
        if find[i][x] == "*":
            cnt += 1
    return cnt

N = int(input())
cookie = [list(input()) for _ in range(N)]

heart_xy = heart(cookie)
left_length = left_hand(cookie, heart_xy)
right_length = right_hand(cookie, heart_xy)
waist_length = waist(cookie, heart_xy)
left_leg_length = left_leg(cookie, heart_xy, waist_length)
right_leg_length = right_leg(cookie, heart_xy, waist_length)

print(heart_xy[0], heart_xy[1])
print(left_length, right_length, waist_length, left_leg_length, right_leg_length)