def solution(n):
    answer = [[0] * n for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    r, c = 0, 0
    for i in range(1, n * n + 1):
        answer[r][c] = i
        
        dr, dc = directions[d]
        nr = r + dr
        nc = c + dc
        
        if nc < 0 or nr < 0 or nc > n - 1 or nr > n - 1 or answer[nr][nc] != 0:
            d = (d + 1) % 4
            dr, dc = directions[d]
            nr = r + dr
            nc = c + dc
        
        r, c = nr, nc
        
    return answer