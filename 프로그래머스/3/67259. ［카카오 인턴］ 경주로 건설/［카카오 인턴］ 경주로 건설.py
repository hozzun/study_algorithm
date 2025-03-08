import heapq

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(board):
    n = len(board)
    pq = []
    count_grid = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    for d in range(4):
        heapq.heappush(pq, (0, 0, 0, d))
        count_grid[0][0][d] = 0
    
    while pq:
        cur_cost, y, x, direction = heapq.heappop(pq)
        
        if (y, x) == (n - 1, n - 1):
            return min(count_grid[y][x])
        
        for d, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = cur_cost + (100 if d == direction else 600)
                
                if new_cost < count_grid[ny][nx][d]:
                    count_grid[ny][nx][d] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx, d))
                
                