from collections import deque

def solution(begin, target, words):

    def bfs(x, time):
        q = deque()
        q.append((x, time))
        visited = set()
        visited.add(x)
        
        while q:
            cur, t = q.popleft()
            if cur == target:
                return t
            
            for next in words:
                diff = [a for a, b in zip(cur, next) if a != b]
                if len(diff) == 1 and next not in visited:
                    q.append((next, t+1))
                    visited.add(next)
                    
        return 0
            
    return bfs(begin, 0)