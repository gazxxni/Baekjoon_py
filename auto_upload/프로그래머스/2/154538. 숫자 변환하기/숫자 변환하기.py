from collections import deque

def bfs(start, target, n):
    q = deque([(start, 0)])
    visited = {start}

    while q:
        cur, cnt = q.popleft()
        
        if cur == target:
            return cnt
        
        for nex in [cur + n, cur * 2, cur * 3]:
            if nex <= target and nex not in visited:
                q.append((nex, cnt+1))
                visited.add(nex)

    return -1
    
def solution(x, y, n):
    return bfs(x, y, n)