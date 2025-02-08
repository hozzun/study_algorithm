import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
def dfs(y, x):
    global visited, graph
    visited[y][x] = True

    for i in range(8):
        ni = y + di[i]
        nj = x + dj[i]
        if 0 <= ni < h and 0 <= nj < w:
            if graph[ni][nj] and not visited[ni][nj]:
                dfs(ni, nj)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)