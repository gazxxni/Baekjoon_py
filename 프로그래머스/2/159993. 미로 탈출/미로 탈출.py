from collections import deque

def bfs(start, target, maps):
    q = deque([(start[0], start[1], 0)])
    visited = {start}
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    n = len(maps)
    m = len(maps[0])
    
    while q:
        cx, cy, t = q.popleft()
        
        if maps[cx][cy] == target:
            return t
        
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and (nx, ny) not in visited:
                q.append((nx, ny, t + 1))
                visited.add((nx, ny))
                
    return -1            

def solution(maps):
    st = None
    le = None

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                st = (i, j)
            elif maps[i][j] == 'L':
                le = (i, j)

    to_lever = bfs(st, 'L', maps)
    to_exit = bfs(le, 'E', maps)

    if to_lever == -1 or to_exit == -1:
        return -1
    
    return to_lever + to_exit