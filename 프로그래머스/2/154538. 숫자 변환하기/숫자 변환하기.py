from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()
    
    while queue:
        cur, num = queue.popleft()
        
        if cur == y:
            return num
        
        if cur in visited:
            continue
        visited.add(cur)
        
        for i in (cur+n, cur*2, cur*3):
            if i <= y and i not in visited:
                queue.append((i, num+1))
    
    return -1