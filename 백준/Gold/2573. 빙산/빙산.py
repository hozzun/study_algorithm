from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] > 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

def cnt_iceberg():
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

def melt():
    melt_cnt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea_count = 0
                for dy, dx in directions:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                        sea_count += 1
                melt_cnt[i][j] = sea_count

    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melt_cnt[i][j])

time = 0
while True:
    cnt = cnt_iceberg()
    if cnt >= 2:
        print(time)
        break
    if cnt == 0:
        print(cnt)
        break
    melt()
    time += 1