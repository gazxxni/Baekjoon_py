from collections import deque

def solution(maps):
    directions = [(1, 0), (0, 1), (-1, 0), (0, - 1)]
    visited = set()
    q = deque()
    q.append((0, 0, 1))
    visited.add((0, 0))
    
    n = len(maps) - 1
    m = len(maps[0]) - 1
    
    while q:
        cx, cy, t = q.popleft()
        
        if (cx, cy) == (n, m):
            return t
        
        for x, y in directions:
            nx = cx + x
            ny = cy + y
            
            if 0 <= nx <= n and 0 <= ny <= m and (nx, ny) not in visited and maps[nx][ny] == 1:
                q.append((nx, ny, t + 1))
                visited.add((nx, ny))
                
    
    return -1