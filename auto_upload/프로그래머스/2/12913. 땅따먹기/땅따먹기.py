def solution(land):
    prev = land[0][:]
        
    for r in range(1, len(land)):
        cur = [0] * (len(land[0]))
        
        for c in range(len(prev)):
            cur[c] = land[r][c] + max(prev[k] for k in range(len(prev)) if k != c)
        
        prev = cur
    
    return max(prev)