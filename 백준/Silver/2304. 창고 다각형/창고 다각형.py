n = int(input())
xy = sorted([tuple(map(int, input().split())) for _ in range(n)])
max_h = max(xy, key=lambda x: x[1])[1]
max_h_idx = 0
for i, (x, y) in enumerate(xy):
    if y == max_h:
        max_h_idx = i
        break

left_area = 0
current_height = xy[0][1]
for i in range(1, max_h_idx + 1):
    left_area += current_height * (xy[i][0] - xy[i-1][0])
    if xy[i][1] > current_height:
        current_height = xy[i][1]

right_area = 0
current_height = xy[-1][1]
for i in range(n - 2, max_h_idx - 1, -1):
    right_area += current_height * (xy[i+1][0] - xy[i][0])
    if xy[i][1] > current_height:
        current_height = xy[i][1]

total_area = left_area + right_area + max_h
print(total_area)