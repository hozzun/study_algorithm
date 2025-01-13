R, C, K = map(int, input().split())
graph = [input().strip() for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * C for _ in range(R)]
ans = 0

def dfs(x, y, distance):
    global ans

    if (x, y) == (0, C - 1) and distance == K:
        ans += 1
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] == '.':
            visited[nx][ny] = True
            dfs(nx, ny, distance + 1)
            visited[nx][ny] = False

visited[R - 1][0] = True
dfs(R - 1, 0, 1)

print(ans)