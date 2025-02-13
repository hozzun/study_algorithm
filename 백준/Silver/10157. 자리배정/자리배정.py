c, r = map(int, input().split())
k = int(input())

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
graph = [[0] * c for _ in range(r)]

if k > (c * r):
    print(0)
    exit()

x, y = 0, 0
graph[y][x] = 1
dir_idx = 0

for i in range(2, k + 1):
    nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]
    while not (0 <= nx < c and 0 <= ny < r) or graph[ny][nx] != 0:
        dir_idx = (dir_idx + 1) % 4
        nx, ny = x + directions[dir_idx][0], y + directions[dir_idx][1]

    x, y = nx, ny
    graph[y][x] = i

print(x + 1, y + 1)