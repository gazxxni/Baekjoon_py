from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    board = [[-1] * 102 for _ in range(102)]
    
    n = len(board)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0

                elif board[i][j] != 0:
                    board[i][j] = 1
    
    start_x, start_y = characterX * 2, characterY * 2
    target_x, target_y = itemX * 2, itemY * 2
    
    q = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    
    
    while q:
        cx, cy, t = q.popleft()
        
        if cx == target_x and cy == target_y:
            return t // 2

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and board[nx][ny] == 1:
                visited.add((nx, ny))
                q.append((nx, ny, t+1))
    
    
    
    return -1