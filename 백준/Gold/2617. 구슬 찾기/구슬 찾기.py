n, m = map(int, input().split())

heavier = [[] for _ in range(n + 1)]
lighter = [[] for _ in range(n + 1)]

for _ in range(m):
    heavy_bead, light_bead = map(int, input().split())
    heavier[heavy_bead].append(light_bead)
    lighter[light_bead].append(heavy_bead)

def dfs(graph, start, visited):
    count = 0
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            count += 1 + dfs(graph, next, visited)
    return count

answer = 0
mid = (n + 1) // 2
for i in range(1, n + 1):
    heavy_visited = [False] * (n + 1)
    heavy_count = dfs(heavier, i, heavy_visited)
    light_visited = [False] * (n + 1)
    light_count = dfs(lighter, i, light_visited)
    if heavy_count >= mid or light_count >= mid:
        answer += 1

print(answer)