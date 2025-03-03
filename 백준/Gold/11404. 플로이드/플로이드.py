import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    print(' '.join(str(0 if graph[i][j] == float('inf') else graph[i][j]) for j in range(1, n + 1)))