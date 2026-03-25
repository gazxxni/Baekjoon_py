from collections import deque

def bfs(start, target, maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = deque([(start[0], start[1], 0)])
    visited = {start}

    while q:
        cr, cc, t = q.popleft()

        if maps[cr][cc] == target:
            return t
        
        for r, c in directions:
            nr = cr + r
            nc = cc + c
            
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] != 'X' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, t + 1))

    return -1


def solution(maps):
    st = None
    le = None
    for r, row in enumerate(maps):
        if 'S' in row:
            st = (r, row.index('S'))
        if 'L' in row:
            le = (r, row.index('L'))
            
        if st and le:
            break
            
    st_to_le = bfs(st, 'L', maps)
    if st_to_le == -1:
        return -1

    le_to_end = bfs(le, 'E', maps)
    if le_to_end == -1:
        return -1

    return st_to_le + le_to_end