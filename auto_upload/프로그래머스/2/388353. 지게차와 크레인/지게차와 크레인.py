from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    graph = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            graph[i + 1][j + 1] = storage[i][j]
                                            
    def bfs():
        visited = set()
        q = deque()
        q.append((0, 0))
        visited.add((0, 0))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n + 2 and 0 <= nc < m + 2 and (nr, nc) not in visited and graph[nr][nc] == 0:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                        
        return visited
    
    for row in requests:
        tar = row[0]
        
        if len(row) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if graph[i][j] == tar:
                        graph[i][j] = 0
                        
        else:
            out = bfs()
            remove = []
            
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if graph[i][j] == tar:
                        for dr, dc in directions:
                            nr, nc = i + dr, j + dc
                            
                            if (nr, nc) in out:
                                remove.append((i, j))
                                break
                                
            for r, c in remove:
                graph[r][c] = 0
                
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] != 0:
                ans += 1
                
    return ans