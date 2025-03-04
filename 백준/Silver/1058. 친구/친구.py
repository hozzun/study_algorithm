from collections import deque

def bfs(i):
    visited = [False] * n
    queue = deque([(i, 0)])
    visited[i] = True
    friends = set()

    while queue:
        current, depth = queue.popleft()

        for next in graph[current]:
            if not visited[next]:
                friends.add(next)
                
                if depth < 1:
                    queue.append((next, depth + 1))
                    visited[next] = True
                    
    return len(friends)

n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    isFriend = input()
    for j in range(n):
        if isFriend[j] == 'Y':
            graph[i].append(j)

answer = max(bfs(i) for i in range(n))
print(answer)