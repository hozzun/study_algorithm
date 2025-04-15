import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(v):
    for i in graph[v]:
        if not par[i]:
            par[i] = v
            dfs(i)

T = int(input())
graph = [[] for _ in range(T+1)]
par = [0] * (T+1)
for _ in range(T-1):
    N, M = map(int, input().split())
    graph[N].append(M)
    graph[M].append(N)

dfs(1)

for i in range(2, T+1):
    print(par[i])