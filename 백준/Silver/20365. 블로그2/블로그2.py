n = int(input())
colors = list(input().strip())
colors.append('X')

blue_check = 1
for i in range(n):
    if colors[i] == 'R':
        if colors[i+1] == 'R':
            continue
        elif colors[i] == 'X':
            continue
        else:
            blue_check += 1

red_check = 1
for i in range(n):
    if colors[i] == 'B':
        if colors[i+1] == 'B':
            continue
        elif colors[i] == 'X':
            continue
        else:
            red_check += 1

print(min(blue_check, red_check))