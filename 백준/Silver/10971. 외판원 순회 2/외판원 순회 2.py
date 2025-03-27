def dfs(start, now, count, total):
    global answer

    if count == n:
        if grid[now][start] != 0:
            answer = min(answer, total + grid[now][start])
        return

    for next in range(n):
        if not visited[next] and grid[now][next] != 0:
            visited[next] = True
            dfs(start, next, count + 1, total + grid[now][next])
            visited[next] = False

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, i, 1, 0)

print(answer)