import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(n, start, end, grid):
    pq = []
    mirrors = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    for d in range(4):
        heapq.heappush(pq, (0, start[0], start[1], d))
        mirrors[start[0]][start[1]][d] = 0

    while pq:
        mirror_count, y, x, direction = heapq.heappop(pq)

        if mirror_count > mirrors[y][x][direction]:
            continue

        if (y, x) == end:
            return mirror_count

        dy, dx = directions[direction]
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != '*':
            if grid[ny][nx] == '!':
                for new_dir in range(4):
                    new_count = mirror_count
                    if new_dir != direction:
                        new_count += 1

                    if new_count < mirrors[ny][nx][new_dir]:
                        mirrors[ny][nx][new_dir] = new_count
                        heapq.heappush(pq, (new_count, ny, nx, new_dir))

            else:
                if mirror_count < mirrors[ny][nx][direction]:
                    mirrors[ny][nx][direction] = mirror_count
                    heapq.heappush(pq, (mirror_count, ny, nx, direction))

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
doors = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == '#': doors.append((i, j))

door1, door2 = doors[0], doors[1]

print(bfs(n, door1, door2, grid))