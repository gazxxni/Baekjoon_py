from collections import deque

def solution(board):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(board)
    
    q = deque([(0, 0, 0, -1)])
    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    for i in range(4):
        visited[0][0][i] = 0
        
    while q:
        cur_x, cur_y, cur_cost, cur_direction = q.popleft()
        
        for i in range(4):
            dx, dy = directions[i]
            nx = cur_x + dx
            ny = cur_y + dy
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if cur_direction == -1 or cur_direction == i:
                    new_cost = cur_cost + 100
                else:
                    new_cost = cur_cost + 600
                
             
                if new_cost < visited[nx][ny][i]:
                    visited[nx][ny][i] = new_cost
                    q.append((nx, ny, new_cost, i))
                    
        
    return min(visited[n-1][n-1])


